#include <cstdio>
using namespace std;
int a[4][4],b[4][4];
int fir[4],sec[4];
int l,r,n;
int i,j,cas;
int main()
{
      freopen("A-small-attempt0.in","r",stdin);
      freopen("A.out","w",stdout);
      scanf("%d",&n);
      for (cas = 1;cas<=n;++cas)
      {

            scanf("%d",&l);
            for(i=0;i<4;++i)
              {
               for(j=0;j<4;++j)
               {
                     scanf("%d",&a[i][j]);
                     if(i==l-1)
                        fir[j]=a[i][j];
               }
              }
            scanf("%d",&r);
            for(i=0;i<4;++i){
               for(j=0;j<4;++j){
                 scanf("%d",&b[i][j]);
                 if(i==r-1)
                    sec[j]=b[i][j];
               }
            }
            bool mul = false,flag = false;
            int ans = 0 ;
            for(i=0;i<4;++i)
            {
                  for(j=0;j<4;++j)
                    if(!flag )
                    {
                          if (fir[i]==sec[j])
                            {
                                  ans= fir[i];
                                  flag = true;
                            }
                    }
                    else
                    {
                          if (fir[i]==sec[j])
                              mul = true;
                    }
            }
       printf("Case #%d: ",cas);
            if(mul)
                  printf("Bad magician!\n");
            else if(flag)
            {
                  printf("%d\n",ans);
            }
            else printf("Volunteer cheated!\n");
      }

      return 0 ;
}
