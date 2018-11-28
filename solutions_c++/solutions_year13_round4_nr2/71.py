#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <deque>
#include <complex>
#include <stack>
#include <queue>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <ctime>
#include <iterator>
#include <bitset>
#include <numeric>
#include <list>
#include <iomanip>
using namespace std;


typedef long long LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;

typedef vector<int> vint;
typedef vector<vector<int> > vvint;
typedef vector<long long> vll, vLL;
typedef vector<vector<long long> > vvll, vvLL;

#define VV(T) vector<vector< T > >

template <class T>
void initvv(vector<vector<T> > &v, int a, int b, const T &t = T()){
	v.assign(a, vector<T>(b, t));
}

template <class F, class T>
void convert(const F &f, T &t){
	stringstream ss;
	ss << f;
	ss >> t;
}


#define REP(i,n) for(int i=0;i<int(n);++i)
#define ALL(v) (v).begin(),(v).end()
#define RALL(v) (v).rbegin(),(v).rend()
#define PB push_back
#define ITR ::iterator


#define MOD 1000000009LL
#define EPS 1e-8


LL n, p, m;

LL calc_y(){
	LL left = 0, right = m;
	while(left < right){
		LL y = (left + right + 1) / 2;
		LL str = y;
		LL len = m + 1;
		bool ok = true;
		LL q = p;
		while(q > 0){
//printf("check(y = %lld, len = %lld, q = %lld, str = %lld)\n",y,len,q,str);
			if(q == len){
				break;
			}
			
			len /= 2;
			if(len < q){
				q -= len;
				str = (str - 1) / 2;
			}
			else{
				ok = (str == 0);
				break;
			}
		}

//printf("%lld: %s\n",y,ok?"ok":"ng");
		if(ok){
			left = y;
		}
		else{
			right = y - 1;
		}
	}
	return left;
}

LL calc_z(){
	LL f = 0, d = 1, len = m + 1, q = p;
	LL z = 0;
	while(q > 0){
//fprintf(stderr,"len: %lld\tq: %lld\tf: %lld\td: %lld\tz: %lld\n",len,q,f,d,z);
		if(len == q){
			z = max(z, f + d * (q - 1));
			break;
		}

		len /= 2;
		if(len < q){
			z = max(z, f + d * 2 * (len - 1));
			f += d;
			q -= len;
		}
		else{
		}
		d *= 2;
	}
	return z;
}

pll solve(){
	cin >> n >> p;
	m = (1LL << n) - 1;

	LL y = calc_y();
	LL z = calc_z();
	return pll(y, z);
}


int main(){
	cout << fixed << setprecision(10);

	int T = 0;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i){
		fprintf(stderr, "%4d / %4d\n", i, T);
		pll res = solve();
		cout << "Case #" << i << ": " << res.first << ' ' << res.second << endl;
	}
}
