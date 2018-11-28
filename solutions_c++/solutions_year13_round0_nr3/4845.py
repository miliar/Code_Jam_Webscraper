#include <stdio.h>
#include <math.h>

int kapil(long long int bc){
    long long int kap=0,ab;
    int kapi;
                    ab=bc;
                while(bc){
                    kapi=bc%10;
                    kap=kap*10+kapi;
                    bc=bc/10;
                }
                if(ab==kap) return 1;
                else return 0;
}
int main(void){

long long int ef,fg,rv ,s;
long long int cd,de;
int sos;
int r,point,pointer=1;
scanf("%d",&sos);
while(sos--){
        rv=0;point=0;fg=0;ef=0;
           scanf("%lld%lld",&cd,&de);
           
           if(cd>1)
           fg=(int)sqrt(cd);
           else fg=cd;
           ef=fg*fg;
           if(ef<cd){ ++fg; ef=fg*fg;}
           else ef=fg*fg;
 
           while(ef<=de){
            
            if(kapil(fg)){
            
                if(kapil(ef)){
              
                 ++point;
              }
            }
            fg++;
            ef=fg*fg;
           } printf("Case#%d: %d\n",pointer,point);
           pointer++;
}
return 0;
}
