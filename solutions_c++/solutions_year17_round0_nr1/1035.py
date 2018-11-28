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
#define M 1005
void RI(){}
template<typename... T>
void RI( int& head, T&... tail ) {
    scanf("%d",&head);
    RI(tail...);
}
using namespace std;
typedef long long LL;
int t,n,k;
char in[M];
int main()
{
	RI(t);
	REP(tt,1,t)
	{
		scanf("%s %d",in+1,&k);
		n=strlen(in+1);

		int ans=0;
		REP(i,1,n-k+1) if(in[i]=='-')
		{
			ans++;
			REP(j,i,i+k-1)
			{
				if(in[j]=='+') in[j]='-';
				else in[j]='+';
			}
		}

		bool flg=true;
		REP(i,1,n) if(in[i]=='-') flg=false;
		printf("Case #%d: ",tt);
		if(flg) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}

