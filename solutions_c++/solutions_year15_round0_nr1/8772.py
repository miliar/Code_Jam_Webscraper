#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <deque>
#include <queue>
#include <bitset>
#include <stack>
#include <set>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iomanip> 
#include <ctime>
using namespace std;

#define sz size()
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second 


typedef long long ll;
typedef vector<ll> vint;
typedef unsigned long long ull;
typedef pair<int, int> pii; 
const int INF=~(1<<31);
const double eps=1e-6;
 
const long double PI = 3.1415926535;
const int MOD=1e9+7;

int n,m; 
int mcmp(pii x,pii y){
	if(x.first+x.second==y.first+y.second) return x.first<y.first;
	return (x.first+x.second<y.first+y.second);
}
int main() {
	freopen("dna10.in", "r", stdin);
	freopen("dna10.out", "w", stdout); 
	int T;cin>>T;
	while(T--){
		string s;
		cin>>s;
		n=s.sz;
		vector<int> a(n),l(n,-1),r(n,n),sum(n);
		rep(i,n){
			a[i]= s[i]=='A' || s[i]=='G';
			if(i)sum[i]+=sum[i-1];
			sum[i]+=1-a[i];
		}

		rep(i,n){
			if(i){
				l[i]=l[i-1];
				if(a[i-1]==0)l[i]=i-1;
			}
		}
		ROF(i,n-2,0){
			r[i]=r[i+1];
			if(a[i+1]==0)r[i]=i+1;
		}
		if(sum[n-1]==0){
			cout<<n;
			puts(" 0");
			continue;
		}
		if(sum[n-1]==n){
			 
			cout<<"0 "<<n<<endl;
			continue;
		}
		int first;
		if(a[0])first=r[0]; else first=0;
		int ans1=0,ans0=0;
		FOR(it,1,40){
			if(it>sum[n-1])break;
			int li=first,ri=first;
			while(ri<n){
				while(ri<n && sum[ri]-(li?sum[li-1]:0)<it)ri=r[ri];
				while(li>=0 && sum[ri]-(li?sum[li-1]:0)>it)li=r[li];
				int t1=l[li]+1,t2=r[ri]-1;
				int cnt1=t2-t1+1-it;
				if(ans0==0 || ((ans1+0.0)/ans0)<0.000001+((cnt1+0.0)/it)){
					if(fabs(((ans1+0.0)/ans0)-((cnt1+0.0)/it))<0.0000001){
						if(cnt1+it>ans1+ans0)ans1=cnt1; ans0=it;
					}else	ans1=cnt1; ans0=it;
				}
				ri=r[ri];
			}
		}
		cout<<ans1<<' '<<ans0<<'\n';
		//
	}
	return 0; 
}
