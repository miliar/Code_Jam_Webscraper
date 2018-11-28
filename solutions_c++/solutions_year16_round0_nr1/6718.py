#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
    int k[10];

int CheckDigit(int n)
{

    while(n>0)
    {
        k[n%10]=1;
        n=n/10;
    }
    for(int i=0;i<10;i++)
    {

        if(k[i]==0)
            return 1;
    }
    return 0;
}
int main()
{
    freopen("al.in","r",stdin);
    freopen("al.out","w",stdout);
    int n,CASE;
    scanf("%d",&CASE);
   for(int C=1;C<=CASE;C++)
   {
       scanf("%d",&n);
       int res=0;
      memset(k,0,sizeof(k));
       for(int t=1;t<=100;t++)
       {
           if(CheckDigit(t*n)==0)
            {res= t*n;
            break;
            }
       }
       if(res==0)
        printf("Case #%d: INSOMNIA\n",C);
       else
        printf("Case #%d: %d\n",C,res);

   }
    return 0;
}
