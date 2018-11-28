#include <iostream>
using namespace std;
const int maxn = 20;
int c[maxn];
void init(int k)
{
     int i,j,x;
     for(i=1;i<=4;i++)
     for(j=1;j<=4;j++)
     {
                     scanf("%d",&x);
                     if(i==k)c[x]++;
     }
}
void work()
{
     int i,s=0,p;
     for(i=1;i<=16;i++)
     if(c[i]==2){++s;p=i;}
     if(s>1){printf("Bad magician!\n");return ;}
     if(s==0){printf("Volunteer cheated!\n");return ;}
     printf("%d\n",p);
}
int main(void)
{
    int tc,i,k;
    scanf("%d",&tc);
    for(i=1;i<=tc;i++)
    {
                      memset(c,0,sizeof(c));
                      printf("Case #%d: ",i);
                      scanf("%d",&k);
                      init(k);
                      scanf("%d",&k);
                      init(k);
                      work();
    }
}
