#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int a[20],i,j,t,x,r,res,resx;
    scanf("%d",&t);
    for(int test=1;test<=t;++test)
    {
            for(i=1;i<=16;++i) a[i]=0;
            scanf("%d",&r);
            for(i=1;i<=4;++i)
            {
                      for(j=1;j<=4;++j)
                      {
                                  scanf("%d",&x);
                                  if(r==i) a[x]++;
                      }            
            }
            scanf("%d",&r);
            for(i=1;i<=4;++i)
            {
                      for(j=1;j<=4;++j)
                      {
                                  scanf("%d",&x);
                                  if(r==i) a[x]++;
                      }            
            }
            res=0;
            for(i=1;i<=16;++i)
                    if(a[i]==2)
                    {
                           ++res;
                           resx=i;
                    }
            if(res==1)      printf("Case #%d: %d\n",test,resx);
            else if(res>1)  printf("Case #%d: Bad magician!\n",test);
            else            printf("Case #%d: Volunteer cheated!\n",test);
    }
}       
