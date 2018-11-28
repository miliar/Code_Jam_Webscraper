#include<cstdio>
#include<algorithm>
#define N 100010
using namespace std;
int test,ii,n,r,c;
int main()
{
    freopen("out.txt","w",stdout);
    scanf("%d",&test);
    for (ii=1;ii<=test;ii++)
    {
    scanf("%d%d%d",&n,&r,&c);
    
    if (n==1)
    printf("Case #%d: GABRIEL\n",ii);
    else
    if (n==2)
    {
             if ((r*c)%2)
             printf("Case #%d: RICHARD\n",ii);
             else
             printf("Case #%d: GABRIEL\n",ii);
    }
    else
    if (n==3)
    {
             if (((r*c)%3==0)&&(r*c>=6))
             printf("Case #%d: GABRIEL\n",ii);
             else
             printf("Case #%d: RICHARD\n",ii);
    }
    else
    if (n==4)
    {
       if (((r*c)%4==0)&&(r*c>=12))
       printf("Case #%d: GABRIEL\n",ii);
       else
       printf("Case #%d: RICHARD\n",ii);
    }
    }
}
