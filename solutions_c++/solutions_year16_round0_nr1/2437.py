#include<bits/stdc++.h>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 
void RI(){}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
using namespace std;
typedef long long LL;
int t,n;
bool vis[11];
char ss[100];
bool rec(LL x)
{
	sprintf(ss, "%lld", x);
	int len = strlen(ss);
	REP(i,0,len-1) vis[ss[i]-'0'] = true;

	REP(i,0,9) if(vis[i]==false) return false;
	return true;
}
int main()
{
	RI(t);
	REP(tt,1,t)
	{
		RI(n);
		MSET(vis, false);

		int ans=-1;
		REP(i,1,100*n)
		{
			if( rec((LL)i*n) )
			{
				ans = i;
				break;
			}
		}

		printf("Case #%d: ",tt);
		if(ans==-1) puts("INSOMNIA");
		else printf("%lld\n", (LL)ans*n);
	}
	return 0;
}

