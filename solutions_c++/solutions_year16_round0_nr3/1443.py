#include<bits/stdc++.h>
#define ll long long
#define pb push_back
using namespace std;



int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    //scanf("%d",&t);

    printf("Case #1:\n");
    int cnt=0;
    for(int i=1;i<=15;i++)
    {
        for(int j=i+1;j<=15;j++)
        {
           for(int m=1;m<=15;m++)
           {
               for(int n=m+1;n<=15;n++)
               {

                   int p=2*i-1;
                   int q=2*j-1;

                   int u=2*m;
                   int v=2*n;
                   //printf("%d %d %d %d\n",p,q,u,v);
                   printf("1");
                   for(int c=30;c>0;c--)
                   {
                       if(c==p || c==q || c==u || c==v)printf("1");
                       else printf("0");
                   }
                   printf("1");
                   for(int c=2;c<=10;c++)printf(" %d",c+1);
                   printf("\n");

                   cnt++;
                   if(cnt==500)return 0;

               }
           }
        }
    }
   // printf("%d\n",cnt);

    return 0;

}
