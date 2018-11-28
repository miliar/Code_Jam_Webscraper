#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<string.h>
#include<cstdlib>

using namespace std;

int main()
{
        freopen("C:\\Users\\ABHISHEK KUMAR\\Desktop\\a.in","r",stdin);
       freopen("C:\\Users\\ABHISHEK KUMAR\\Desktop\\b.out","w",stdout);
        int t,i,j,n,m,k;
        int d=0,wa=0;
        double a,b,c,e,f,x,y;
        double ar[1100];
        double br[1100];
        scanf("%d",&t);
        k=t;
        while(t--)
        {
                d=0,wa=0;
                scanf("%d",&n);
                int c[n + 1];
                int c2[n+1];
                for(i=0;i<n;i++)
                        scanf("%lf",&ar[i]);
                for(i=0;i<n;i++) {
                        scanf("%lf",&br[i]);
                        c[i] = 0;
                        c2[i] = 0;
                }
                  sort(ar,ar+n);
                  sort(br,br+n);
                  int ii=0,jj=0,va=n-1;
                  for(i=n-1;i>=0;i--)
                  {
                          for(j=n-1;j>=0;j--)
                          {
                                  if(br[j] > ar[i] && c[j] == 0) {
                                        c[j] = 1;
                                        break;
                                  }

                          }
                          if (j == -1){
                                wa++;
                          }
                          for (j = n-1; j >= 0; j--) {
                                if (ar[j] > br[i] && c2[j] == 0)
                                        {
                                        d++;
                                        c2[j] =1;
                                        break;
                                }
                        }

                  }



                printf("Case #%d: %d %d\n",k-t,d,wa);
        }
        return 0;
}
