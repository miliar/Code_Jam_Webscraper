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
	int a,b,ar[17]={},i,j,ans,flag1=0,flag2=0,temp;
	cin >> a;
	for(i=0; i<4; i++)
	{
	    for(j=0; j<4; j++)
	    {
		cin >> temp;
		if(i==(a-1))ar[temp]++;
	    }
	}
	cin >> b;
	for(i=0; i<4; i++)
	{
	    for(j=0; j<4; j++)
	    {
		cin >> temp;
		if(i==(b-1))ar[temp]++;
	    }
	}
	printf("Case #%d: ",p-t);
	for(i=1; i<=16; i++)
	    if(ar[i]==2){flag2++;ans=i;}
	if(flag2==0)printf("Volunteer cheated!\n");
	else if(flag2==1)printf("%d\n",ans);
	else printf("Bad magician!\n");
    }
    return 0;
}
