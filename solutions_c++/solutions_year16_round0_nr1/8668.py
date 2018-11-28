#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
int t, n, a, c, d[20], cont;
int main()
{
    scanf("%d",&t);
    for (int i=1; i<=t; i++)
    {
       scanf("%d",&n);
       c=0; cont=0;
       for (int j=0; j<=9; j++) 
       d[j]=0;
       while (cont<=100000 && c<10)
       {
          cont++;
          a=n*cont;
          while (a>0)
          {
            d[a%10]++;
            if (d[a%10]==1) c++;
            a=a/10;
          }
       }
       if (cont==100001)
       printf("Case #%d: INSOMNIA\n",i);
       else
       printf("Case #%d: %d\n",i,n*cont); 
    }
    scanf("%d",&t);
    return 0; 
} 
