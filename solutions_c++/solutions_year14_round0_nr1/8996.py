#include<cstdio>
#include<cstring>
using namespace std;

int a,b,t;
int ca=1;
int m1[7],m2[7],c;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    int i,j;
    while(t--)
    {
        scanf("%d",&a);
        for(i=1;i<=4;i++)
        {
          for(j=1;j<=4;j++)
          {
              if(i==a)
              scanf("%d",&m1[j]);
              else
              scanf("%d",&c);
          }
        }
        scanf("%d",&b);
        for(i=1;i<=4;i++)
        {
          for(j=1;j<=4;j++)
          {
              if(i==b)
              scanf("%d",&m2[j]);
              else
              scanf("%d",&c);
          }
        }
        int same=0;
        int ans=-1;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            if(m1[i]==m2[j])
            {
                ans=m1[i];
                same++;
            }
        }
        printf("Case #%d: ",ca++);
        if(same==0)
        printf("Volunteer cheated!\n");
        else if(same==1)
        printf("%d\n",ans);
        else
        printf("Bad magician!\n");

    }
    return 0;
}
