#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())

#define S(x) scanf("%d",&x)
#define S1(x) scanf("%lld",&x)
#define P(x) printf("%d\n",x)
#define Sd(x) scanf("%lf",&x)
#define Pd(x) printf("%0.10lf\n",x)
#define P1(x) printf("%lld\n",x)
#define Ps(x) printf("%d ",x)
#define P1s(x) printf("%lld ",x)
#define St(x) scanf("%s",x)
#define Pt(x) printf("%s",x)
#define Sa(a,n) for(i=0;i<n;i++){scanf("%lld",&a[i]);}
#define Pa(a,n) for(i=0;i<n;i++){printf("%lld ",a[i]);}putchar('\n')
#define Y printf("RICHARD\n")
#define N printf("GABRIEL\n")
#define mod 1000000007
#define ll long long

ll power(ll b, ll e) {
    ll p = 1;
    while (e > 0) {
        if(e&1) {
            p = (p*b)%mod;
        }
        e = e>>1;
        b = (b * b)%mod;
    }
    return p;
}
/*
ll inp()
{
	ll n=0,s=1;
	char c;
	for(c=getchar_unlocked();c<48||c>58;c=getchar_unlocked())
	if(c=='-')s=-1;
	for(;c>47&&c<59;c=getchar_unlocked())
	n=n*10+c-48;
	return n*s;
}
*/
bool ans[5][5][5];
int main()
{
	ll n,i,t,j,k,pmax,f,sub,mn,x,r,c;
	memset(ans,false,sizeof(ans));
	for(i=1;i<5;i++)
        for(j=1;j<5;j++)
        {
            if((i*j)%2)
                ans[2][i][j]=true;
            if((i*j)%3)
                ans[3][i][j]=true;
            if((i*j)%4)
                ans[4][i][j]=true;

            if(i==1||j==1)
            {
                ans[3][i][j]=true;
                ans[4][i][j]=true;
            }
        };
    ans[4][2][4]=true;
    ans[4][4][2]=true;
    ans[4][2][2]=true;
	for(S1(t),k=1;k<=t;k++)
	{
	    printf("Case #%lld: ",k);
	    S1(x);
	    S1(r);
	    S1(c);
	    ans[x][r][c]?Y:N;
	}
	return 0;
}


