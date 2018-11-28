#include<bits/stdc++.h>
using namespace std;
int ar[15];
bool IfPresent()
{
    int i,flag=0;
    for(i=0;i<=9;i++)
    {
        if(ar[i]==0){
            flag=1;
            break;
        }
    }
    return flag;
}
void Numbers(int n)
{
    int nw;
    while(n!=0)
    {
        nw=n%10;
        ar[nw]=1;
        n/=10;
    }
    return;
}
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int t,cs,i,j,n,res;
    scanf("%d",&t);
    for(cs=1;cs<=t;cs++)
    {
        memset(ar,0,sizeof(ar));
        scanf("%d",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",cs);
            continue;
        }
        i=1;
        while(1)
        {
            res=n*i;
            Numbers(res);
            if(IfPresent()==0)
            {
                printf("Case #%d: %d\n",cs,res);
                break;

            }
            i++;
        }

    }

    return 0;
}
