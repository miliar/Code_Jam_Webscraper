#include <iostream>
#include <cstdio>
#include <string.h>

using namespace std;
int main(){
    
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    
    int T, cas=0, lef,rig,mid;
    
    double C,X,F,ans,tmp;
    
    scanf("%d",&T);
    while(T--){
         cas++;
         scanf("%lf%lf%lf",&C,&F,&X);
         printf("Case #%d: ",cas);
         if(X<=C){
            printf("%.6lf\n",X/2.0);
         }
         else{
              rig = (int) (X/C);
              ans = X/2.0;
              tmp=0;
              for(int i = 0; i<=rig; i++){
                  tmp = tmp+ C/(2.0+F*(i+0.0)); 
                  if((tmp + X/(2.0+F*(i+1.0))) < ans ){
                       ans = (tmp + X/(2.0+F*(i+1.0)));
                       //printf("\n ans  %.7lf \n",ans);
                  }  
              }
              printf("%.7lf\n",ans);     
         }
    }
}
