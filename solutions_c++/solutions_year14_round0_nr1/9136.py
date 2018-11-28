#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <sstream>
using namespace std;

#define FOR(i,x,n) for(int i=x;i<n;++i)
#define RFOR(i,x,n) for(int i=x;i>=n;--i)
#define ST 0.000000001
#define MOD 1000000007
#define pb(a) push_back(a)
#define b() begin()
#define e() end()
#define CLR(a,x) memset(a,x,sizeof(a))
#define sz(x) (int)x.size()
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define LL long long
#define VI vector < int >
#define VUI vector < unsigned int >
#define VLL vector < long long >
#define VD vector < double >
#define PII pair < int , int >
#define INF 2147483647
#define LLINF 9223372036854775807
#define si(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define sd(a) scanf("%lf",&a)

int T, x, r, cnt[20];

int main()
{
	cin>>T;
	FOR(t,1,T+1){
		FOR(i,0,17)
			cnt[i] = 0;
		cin>>r;
		FOR(i,0,4)
			FOR(j,0,4){
				cin>>x;
				if(i+1==r)
					++cnt[x];
			}
		cin>>r;
		FOR(i,0,4)
			FOR(j,0,4){
				cin>>x;
				if(i+1==r)
					++cnt[x];
			}
		int noa = 0, ans = -1;
		FOR(i,1,17)
			if(cnt[i]==2){
				++noa;
				ans = i;
			}
		cout<<"Case #"<<t<<": ";
		if(noa > 1)
			cout<<"Bad magician!"<<endl;
		else if(noa == 0)
			cout<<"Volunteer cheated!"<<endl;
		else
			cout<<ans<<endl;
	}	
	return 0;
}