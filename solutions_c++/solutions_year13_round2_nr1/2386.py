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
int a[100],y;
int func(int ans,int mote,int i)
{
   // cout<<ans<<" "<<mote<<" "<<i;
    if(i==y)
        return ans;
    if(mote>a[i])
        return(func(ans,mote+a[i],i+1));
    else
    return min(func(ans+1,2*mote-1,i),func(ans+1,mote,i+1));
}
int main()
{
int t,p;
int i,j,x,count=0,pos1,pos2;
FILE * fp,*fw;
fp=fopen("A-small-attempt0.in","r");
fw=fopen("output.txt","w");
fscanf(fp,"%d",&t);
for(p=1;p<=t;p++)
    {
    fscanf(fp,"%d %d",&x,&y);
    //cout<<x;
    for(i=0;i<y;i++)
        fscanf(fp,"%d",&a[i]);
    if(x==1)
        fprintf(fw,"Case #%d: %d\n",p,y);
    else
        {sort(a,a+y);
        fprintf(fw,"Case #%d: %d\n",p,func(0,x,0));
        }
    }

return 0;
}
