//#include<bits/stdc++.h> 
#include<deque>
#include<complex>
#include<cmath>
#include<algorithm>
#include<limits>
#include<vector>
#include<bitset>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<map>
#include<list>
#include<set>
#include<stack>
#include<queue>
#include<string>
#include<utility>
#include<cassert>
#include<functional>
#include<numeric>
#include<iomanip>
#include<cctype>
#include <sstream> // istringstream>> ostring stream<<
#include <iostream> 
#include <iomanip>
using namespace std;
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (4) << f << endl; Prints x.xxxx
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define FORIT(it,m)    for(it=m.begin();it!=m.end();it++)
#define ll long long int
#define llu unsigned long long int
#define P(k) printf("%d\n", k)
#define si(n) scanf("%d",&n)
#define sc(n) scanf("%c",&n)
#define sl(n) scanf("%lld",&n)
#define slu(n) scanf("%llu",&n)
#define sf(n) scanf("%f",&n)
#define sd(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ALL(v)          (v).begin(), (v).end()
#define RALL(v)         (v).rbegin(), (v).rend()
#define SZ(V) (int)V.size()
#define checkbit(n,b)   (((n)>>(b))&1)
#define FILL(a,b) memset(a,b,sizeof(a))
#define sqr(x) ((x)*(x))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define all(a) (a).begin(),(a).end()
#define DREP(a)	sort(all(a)); a.erase(unique(all(a)),a.end())
#define ALLOC(type, n) (type *) malloc((n)*sizeof(type))
void read(string& s) {  char buf[650000]; gets(buf); s = buf; }
const double PII=acos(-1.0);
const double EPS=1e-11;
#define MOD 1000000007
int mp[17];
int main()
{
    freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T,t=1,x,y,temp;
    si(T);
    while(t<=T)
    {
    	si(x);
    	FILL(mp,0);
    	for(int i=1;i<=4;i++)
    	{
    		for(int j=1;j<=4;j++)
    		{
    			si(temp);
				if(i==x)
    			mp[temp]++;
    		}
    	}
    	si(y);
    	for(int i=1;i<=4;i++)
    	{
    		for(int j=1;j<=4;j++)
    		{
    			si(temp);
				if(i==y)
				mp[temp]++;
			}
    	}
    	int p,count=0,res;
    	for( p=1;p<=16;p++)
    	{
    		if(mp[p]==2)
    		{
    			res=p;
				count++;
    		}
    	}
    	if(count==0)
    	printf("Case #%d: Volunteer cheated!\n",t);
    	else if(count==1)
    	printf("Case #%d: %d\n",t,res);
    	else
    	printf("Case #%d: Bad magician!\n",t);
    	t++;
    	
    }
    getchar();
    return 0;
}
/*

*/
