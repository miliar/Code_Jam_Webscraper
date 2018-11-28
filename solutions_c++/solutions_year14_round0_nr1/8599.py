//author : @kcahdog
#include <bits/stdc++.h>

using namespace std;
/* General Declarations */
#define INF	        1000000007
#define LL	        long long
#define INFL	    (LL)1000000007
//INTEGERS
#define si(n)		scanf("%d",&n)
#define s2i(n,m)	scanf("%d %d",&n,&m)
#define s3i(m,n,k)	scanf("%d %d %d",&m,&n,&k)
#define pi(n)		printf("%d\n",n);
#define pis(n)		printf("%d ",n);
//CHAR AND STRING
#define sc(c)		scanf("%c",&c)
#define ss(s)		scanf("%s",s)
#define pc(n)		printf("%c\n",n);
#define pcs(n)		printf("%c ",n);
//FLOAT AND DOUBLE
#define sf(n)		scanf("%f",&n)
#define pf(n)		printf("%f\n",n)
#define slf(n)		scanf("%lf",&n)
#define plf(n)		printf("%lf\n",n)
//LONG LONG
#define sll(n)		scanf("%lld",&n)
#define pll(n)		printf("%lld\n",n)
#define plls(n)		printf("%lld ",n)

#define pline()		printf("\n");

LL gcd(LL a, LL b){ LL temp; while(b>0)	{ temp= b; b=a%b; a=temp;}	return a;}

#define FOR(x,a,b)	    for( x=a;x<b;x++)
#define fr(i,n)	        for( i=0;i<n;i++)
#define PRINT(v,i,n)	fr(i,n){printf("%d ",v[i]);}printf("\n");
#define PRINTLL(v,i,n)	fr(i,n){printf("%lld ",v[i]);}printf("\n");
#define sortrev(arr,n)     sort(arr,arr+n,greater<int>())
#define SIZE 4

int main()
{
int i,m,j,n,t,k=0;
int cnt;
int arr[4][4];
int a2[4][4];
int ans[17];
si(t);					//NO OF TEST CASES
fr(k,t)
{
fr(i,17)
    ans[i]=0;
si(m);
fr(i,4)
    fr(j,4)
        si(arr[i][j]);
fr(i,4)
    ans[arr[m-1][i]]++;
si(n);
fr(i,4)
    fr(j,4)
        si(a2[i][j]);
fr(i,4)
    ans[a2[n-1][i]]++;
cnt=0;
int num;
fr(i,17)
    if(ans[i]>1)
    {
        cnt++;
        num=i;
    }
if(cnt==1)
    printf("Case #%d: %d\n",k+1,num);
if(cnt==0)
    printf("Case #%d: Volunteer cheated!\n",k+1,num);
if(cnt>1)
    printf("Case #%d: Bad magician!\n",k+1);

}	//end of t loop
return 0;
}
