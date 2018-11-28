#include<bits/stdc++.h>
using namespace std;
int r,c,a[20],ans;
void gen(int x,int y)
{
    if(x==r*c)
    {
        if(y)return;
        int i,j,co=0;
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(a[i*c+j])
                {
                    if(i>0&&a[(i-1)*c+j])co++;
                    if(j>0&&a[i*c+j-1])co++;
                }
            }
        }
        ans=min(ans,co);
    }
    else
    {
        a[x]=0;
        gen(x+1,y);
        if(y)
        {
            a[x]=1;
            gen(x+1,y-1);
        }
    }
}
int main()
{
    freopen("B-in.txt","r",stdin);
    freopen("B-out.txt","w",stdout);
    int t,cas,n,i;
    scanf("%d",&t);
    for(cas=1;cas<=t;cas++)
    {
        ans=2000000000;
        scanf("%d %d %d",&r,&c,&n);
        gen(0,n);
        printf("Case #%d: %d\n",cas,ans);
    }
}
