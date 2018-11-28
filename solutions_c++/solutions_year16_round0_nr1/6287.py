#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("SHIVLI.in","w",stdout);
    int t,j;
    int a[11];
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
       int r,k,c;
       long long n,temp,i;
       bool flag=0;
       for(i=0;i<=9;i++)
         a[i]=0;
       scanf("%lld",&n);
       if(n==0)
       printf("Case #%d: INSOMNIA\n",j);
       else
       {
       i=1;
       while(1)
       {   c=0;
           temp=i*n;
           while(temp)
          {
           r=temp%10;
           a[r]++;
           temp=temp/10;
          }

          for(k=0;k<=9;k++)
            if(a[k]!=0)  c++;
           if(c==10)
             break;
          i++;
       }
       printf("Case #%d: %lld\n",j,i*n);
       }
    }
    return 0;
}
