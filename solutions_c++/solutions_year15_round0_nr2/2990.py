#include<stdio.h>
#include<algorithm>
using namespace std;
int s[1007];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cascc=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,maxxx=-1;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
            scanf("%d",&s[i]),maxxx=max(maxxx,s[i]);
        int suuum=0,minnn=100007;
        for(int i=1;i<=maxxx;i++)
        {
            suuum=0;
            for(int j=0;j<n;j++)
                if(s[j]>i)suuum+=(s[j]-1)/i;
            suuum+=i;
            minnn=min(minnn,suuum);
        }
        printf("Case #%d: %d\n",cascc++,minnn);
    }
    return 0;
}
