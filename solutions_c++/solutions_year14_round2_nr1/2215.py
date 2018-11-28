#include<vector>
#include<iostream>
#include<stdio.h>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<climits>
#include<sstream>
#include<string>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<bitset>
 
#define FL(i,a,b) for(int i=a;i<b;i++)
#define FOR(i,n) for(int i=0;i<n;i++)
#define SORTF(x) sort(x.begin(),x.end(),func);
#define SORT(x) sort(x.begin(),x.end())
#define pb(x) push_back(x)
#define ll long long
#define SET(v, val) memset(v, val, sizeof(v)) ;
#define RSORT(v) { SORT(v) ; REVERSE(v) ; }
#define ALL(v) v.begin(),v.end()
#define REVERSE(v) { reverse(ALL(v)) ; }
#define UNIQUE(v) unique((v).begin(), (v).end())
#define RUNIQUE(v) { SORT(v) ; (v).resize(UNIQUE(v) - (v).begin()) ; }
#define fill(x,n) memset(x,n,sizeof(x))
#define si(x) scanf("%d",&x)
#define si2(x,y) scanf("%d %d",&x,&y)
#define si3(x,y,z) scanf("%d %d %d",&x,&y,&z)
 
#define ss(x) scanf("%s",x)
 
#define sc(x) scanf("%c",&x)
 
#define sf(x) scanf("%f",&x)
 
#define sl(x) scanf("%lld",&x)
#define sl2(x,y) scanf("%lld %lld",&x,&y)
#define sl3(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)
 
#define ll long long
#define str string
#define lli long long int
#define ch char
#define fl float
 
#define out(x) cout << x << endl
#define out2(x,y) cout << x << " " << y << endl
#define out3(x,y,z) cout << x << " " << y << " " << z << endl
 
#define printi(x) printf("%lld\n",x)
#define printi2(x,y) printf("%lld %lld\n",x,y)
#define printi3(x,y,z) printf("%lld %lld %lld\n",x,y,z)
#define prints(x) printf("%s\n",x)
 
using namespace std;

int main()
{
	int t,cas=1;
	cin >> t;
	ll n;

	while(t!=0) 
	{
		cin >> n;
		string s[n];
		FOR(i,n)
			cin >> s[i];
		ll l1 = s[0].length();
		ll l2 = s[1].length();
		ll x1=1,x2=1,f=1;
		ll ans=0;
		while((x1<l1 || x2<l2) && f==1){
			if(s[0][x1]!=s[1][x2]){
				if( x1 < l1 && s[0][x1] == s[1][x1-1]){
					x1++;
					ans++;
				}
				else if(x2 < l2 && s[1][x2] == s[1][x2-1]){
					x2++;
					ans++;
				}
				else{
					f=0;
					break;
				}
			}
			else{
				x1++;
				x2++;
			}

		}
		if(f==0) 
			cout << "Case #" << cas <<": " << "Fegla Won" << endl;
		else
			cout << "Case #" << cas << ": " << ans << endl;
		cas++;
		t--;
	}
	return 0;
}
