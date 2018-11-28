#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,a[10][10],j,l,x,i,b[100000],tmp,counti;
    char s[100000];
    a[1][2]=a[2][1]=a[3][4]=2;
    a[1][3]=a[3][1]=a[4][2]=3;
    a[1][4]=a[4][1]=a[2][3]=4;
    a[1][1]=1;
    a[2][2]=a[3][3]=a[4][4]=-1;
    a[4][3]=-2;
    a[2][4]=-3;
    a[3][2]=-4;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%d %d",&l,&x);
        scanf("%s",s);
        for(i=0;i<l;i++)
        b[i]=s[i]-'g';
        for(i=l;i<l*x;i++) b[i]=b[i%l];
        tmp=1,counti=0;
        for(i=0;i<l*x;i++)
        {
            if(tmp<0) tmp=-a[-tmp][b[i]];
            else tmp=a[tmp][b[i]];
            if(tmp==counti+2)
            {
                counti++;
                tmp=1;
            }
        }
        if(counti==3 && tmp==1) printf("Case #%d: YES\n",j);
        else printf("Case #%d: NO\n",j);
    }
}
