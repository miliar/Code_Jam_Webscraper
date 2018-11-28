#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <complex>
#include <numeric>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <deque>
#include <queue>
#include <set>
#include <map>

#include <unordered_map>
#include <unordered_set>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<long double,long double> pdd;
#define FR first
#define SC second

int n;
long double v, x;
vector <pdd> src;
vector <long double> t;

const long double eps = 1e-14;
inline bool isLess(long double a, long double b){
	return a+eps < b;
}
template <class T> bool isLarger(T a, T b){
	return isLess(b,a);
}
template <class T> bool isEqual(T a, T b){
	return !(isLess(a,b) || isLess(b,a));
}

long double temperature(){
	long double vol = 0;
	long double sum = 0;
	FOR(i,0,n){
		sum += t[i]*src[i].FR*src[i].SC;
		vol += t[i]*src[i].SC;
	}
	return sum/vol;
}

long double volume(){
	long double vol = 0;
	FOR(i,0,n){
		vol += t[i]*src[i].SC;
	}
	return vol;
}

void solve(){
	long double temp = temperature();
	if(isLess(x,temp)){
		int i = n;
		do{
			i--;
			t[i] = 0;
			temp = temperature();
		}while(isLess(x,temp));
		long double lo = 0, hi = 1;
		while(isLess(lo, hi)){
			long double mid = (lo+hi)/2;
			t[i] = mid;
			temp = temperature();
			if(isLess(x,temp))
				hi = mid;
			else
				lo = mid;
		}
		t[i] = lo;
	}
	else{
		int i = -1;
		do{
			i++;
			t[i] = 0;
			temp = temperature();
		}while(isLess(temp,x));
		long double lo = 0, hi = 1;
		while(isLess(lo,hi)){
			long double mid = (lo+hi)/2;
			t[i] = mid;
			temp = temperature();
			if(isLess(temp,x))
				hi = mid;
			else
				lo = mid;
		}
		t[i] = lo;
	}
}

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(cnt,0,T){
		cin >> n >> v >> x;
		src.resize(n);
		t.resize(n);
		FOR(i,0,n){
			cin >> src[i].SC >> src[i].FR;
		}
		sort(src.begin(), src.end());

		cout << "Case #" << cnt+1 << ": ";
		if(isLarger(src[0].FR,x) || isLess(src[n-1].FR,x))
			cout << "IMPOSSIBLE\n";
		else{
			long double ans = 1e10;
			long double tt = 1;
			FOR(cnt,0,8){
				fill(t.begin(), t.end(), tt);
				solve();
				ans = min(ans, v/volume()*tt);
				tt *= 10;
			}
			cout << fixed << setprecision(10) << ans << '\n';
		}
	}

	return 0;
}
