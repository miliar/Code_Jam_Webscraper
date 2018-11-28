#include<cstdio>
#include<algorithm>
using namespace std;
double ar[100000],br[100000],mark[100000],l,m;
int e1,e2,s1,s2,t,j,num,k,z=0;
int i,cnt,n;
int main()
{    freopen("m.in","r",stdin);
    freopen("k.out","w",stdout);
scanf("%d",&t);
while(t--)
{
scanf("%d",&n);
k=n;
for(i=0;i<n;i++)
scanf("%lf",&ar[i]);

for(i=0;i<n;i++)
scanf("%lf",&br[i]);
z++;

for(i=0;i<=n;i++)
mark[i]=0;
sort(ar,ar+n);
sort(br,br+n);

num=0;
cnt=0;
s1=0;
s2=0;
e1=n-1;
e2=n-1;
//printf("hello\n");
while(n--)
{
    if(ar[e1]>br[e2])
    {
        cnt++;
    e2--;
    e1--;
    }
    else
    if(ar[e1]<br[e2])
    {
        e2--;
    s1++;
    }
   // printf("s1=%d s2=%d e1=%d e2=%d\n",s1,s2,e1,e2);
    //printf("cnt==%d\n",cnt);
}
for(i=0;i<k;i++)
{   l=0;
    for(j=0;j<k;j++)
    {
        if(ar[i]<br[j]&&mark[j]==0)
        {
            mark[j]=1;
           // printf("hello %d k==%d\n",i,k);
            l=1;
            break;

    }

}




if(l==0)
    num++;






}

















printf("Case #%d: %d %d\n",z,cnt,num);













}


return 0;
}
