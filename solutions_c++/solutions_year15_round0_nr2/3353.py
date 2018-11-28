#include<stdio.h>
#include<algorithm>
using namespace std;
int s[1007],suuum,minn;
 int n,maxxx=-1;
void dongtai()
{
    for(int i=1;i<=maxxx;i++)
        {
            suuum=0;
            for(int j=0;j<n;j++)
                if(s[j]>i) suuum+=(s[j]-1)/i;
            suuum+=i;
            minn=min(minn,suuum);
        }
}

int main()
{
  // freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {

        scanf("%d",&n);
        for(int i=0;i<n;i++)
            {scanf("%d",&s[i]);
            maxxx=max(maxxx,s[i]);}
         suuum=0;
         minn=99999;
        dongtai();
        printf("Case #%d: %d\n",cas++,minn);
    }
    return 0;
}
