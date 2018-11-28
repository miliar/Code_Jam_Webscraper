#include<stdio.h>
using namespace std;
char a[1024];
int main()
{
    freopen("input21.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,i,j,cs,l,ans,csn;
    scanf("%d",&t);
    csn=1;
    while(t--)
    {
        scanf("%d %s",&l,a);
        cs=a[0]-'0';
        ans=0;
        for(i=1;i<=l;i++)
        {
            if(cs>=i)
            {
                cs=cs+(a[i]-'0');
            }
            else
            {
                ans=ans+i-cs;
                cs=i+(a[i]-'0');
            }
        }
        printf("Case #%d: %d\n",csn,ans);
        csn++;
    }
    return 0;
}
