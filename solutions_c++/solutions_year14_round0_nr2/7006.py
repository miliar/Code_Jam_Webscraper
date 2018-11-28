#include <bits/stdc++.h>

#define FI(ii,aa,bb) for(int ii=aa;ii<=bb;ii++)
#define F(ii,aa,bb) for(int ii=aa;ii<bb;ii++)
#define TF(ii,aa,bb) for(int ii=aa;ii>=bb;ii--)

using namespace std;

double go,c,ext;
int TEST;

int main(void){

      freopen("gir11.in","r",stdin);freopen("cik11.out","w",stdout);
      scanf("%d",&TEST);FI(t,1,TEST)
      {
            scanf("%lf %lf %lf",&c,&ext,&go);
            double money=0,ans=0,pro=2.0;

            if(c>=go){

                  printf("Case #%d: ",t);

                  printf("%.7lf\n",go/2.0);

                  continue;
            }while(go>money){
                        ans+=(c-money)/pro; money=c;
                        if((go-money) / pro > go/(pro+ext))
                  {
                        pro+=ext;
                        money-=c;
                  }
                  else
                  {
                        ans+=(go - money) / pro; money=go;
                  }
            }
            printf("Case #%d: ",t);printf("%.7lf\n",ans);
      }
      return 0;
}
