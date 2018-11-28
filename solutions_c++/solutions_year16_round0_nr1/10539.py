#include<bits/stdc++.h>
using namespace std;
int t,k,d;
long long y,x,n,z;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin>>t;bool flag;
    for(int i=1;i<=t;i++)
    {
        int a[10]={0};
        bool flag=false;int k=1;
        scanf("%I64d",&x);
        int z=x;
        if(x==0) printf("Case #%d: INSOMNIA\n",i);
        else{
        while(1)
        {
            n=z;
            while(n>0)
            {
                d=n%10;
                a[d]=1;
                n=n/10;
            } y=x*k;
            for(int j=0;j<10;j++)
            {
                if(a[j]==0) break;
                if(j==9&&a[j]==1) flag=true;
            }
            k++;
            z=x*k;
            if(flag){break;}
        }
        if(flag)
        printf("Case #%d: %I64d\n",i,y);
        else
        printf("Case #%d: INSOMNIA\n",i);}
    }
    return 0;
}
