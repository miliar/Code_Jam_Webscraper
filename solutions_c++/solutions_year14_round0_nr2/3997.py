#include <stdio.h>
#include <conio.h>

int main(){
    float C,F,X;
    int n;
    //freopen("B-large.in","r",stdin);
    
    //freopen("B-large.out","w",stdout);
    scanf("%d",&n);
    for(int i = 0; i < n;i++){
        scanf("%f %f %f",&C,&F,&X);
        double cps,ans,time,jawab;
        time = 0;
        cps = 2;
        
        double temp;
        double pre;
        jawab = 0;
        pre = X/2;
        do{
            
            //printf("%.7f %.7f\n",C/cps,X/cps);
            jawab = jawab + C/cps;
            cps+=F;
            temp = jawab + X/(cps);
            //printf("%.7f\n",jawab);
            if(pre > temp){
                pre = temp;
            }
            else break;
            //getch();
        }while(1);
        printf("Case #%d: %.7f\n",i+1,pre);
        
    };
    return 0;
}
