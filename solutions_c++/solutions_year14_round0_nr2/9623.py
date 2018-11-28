#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,b) for(i=0;i<b;i++)
#define rep1(i,b) for(i=1;i<=b;i++)
#define pdn(n) printf("%d\n",n)
#define sl(n) scanf("%lld",&n)
#define sd(n) scanf("%d",&n)
#define pn printf("\n")
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
#define MOD 1000000007
LL mpow(LL a, LL n) 
{LL ret=1;LL b=a;while(n) {if(n&1) 
ret=(ret*b)%MOD;b=(b*b)%MOD;n>>=1;}
return (LL)ret;}
int main()
{
    int t,p;
    cin >> t;
    p=t;
    while(t--)
    {
	printf("Case #%d: ",p-t);
	double c,f,x,ans=1000000000000.00;
	int i,j;
	cin >> c >> f >> x;
	for(i=0; i<10000; i++)
	{
	    double cur=0;
	    for(j=1; j<=i; j++)
		cur=cur+(c/(2.0+(double)(j-1)*f));
	    cur+=x/(2.0+(double)i*f);
	    if(cur<ans)ans=cur;
	}
	printf("%.8lf\n",ans);
    }
    return 0;
}

