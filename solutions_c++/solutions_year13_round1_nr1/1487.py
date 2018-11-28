#include<iostream>
#include<map>
#include<vector>
#include<set>
#include<string>
#include<stack>
#include<queue>
#include<deque>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

#define mod 1000000007
#define pinf 2147483647
#define ninf -2147483648
#define FOR(i,a,b) for(i=a;i<b;i++)
#define s(a) scanf("%d",&a)
#define lls(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a);
#define p(a) printf("%d",a)
#define llp(a) printf("%lld",a)
#define ps(a) printf("%s",a);
#define nline printf("\n")
#define pc(a) printf("%c",a)
#define ll long long
#define MAX(a,b,c) ((a>b)?(a>c?a:c):(b>c?b:c))
#define MIN(a,b,c) ((a<b)?(a<c?a:c):(b<c?b:c))

int main()
{
int t,p,r,T;
char ch;
FILE * fp,*fw;
fp=fopen("A-small-attempt0.in","r");
fw=fopen("output.txt","w");
fscanf(fp,"%d",&T);
//fprintf(fw,"t=%d",T);
for(p=1;p<=T;p++)
    {
    int a,b,j,k,ans=0,no=0;
    fscanf(fp,"%d %d",&r,&t);
    j=0;
    a=r;
    b=r+1;
    while(ans<t)
        {
        ans+=((r+1)*(r+1)-r*r);
        no++;
        r+=2;
        }
    if(ans!=t)
        no-=1;
    fprintf(fw,"Case #%d: %d\n",p,no);
    }
return 0;
}
