#include<stdio.h>
#include<stdlib.h>



int main(){
    double c,f,x,ans,temp,speed,t;
    int y,cas=1;
    int i,j;
    scanf("%d",&y);
    while(y--){
        scanf("%lf%lf%lf",&c,&f,&x);
        ans=x/2;
        for(speed=2,t=0;;){
            t=t+c/speed;
            speed+=f;
            temp=t+x/speed;
            if(ans>temp)
                ans=temp;
            else
                break;
        }
        printf("Case #%d: %.7lf\n",cas++,ans);

    }




    return 0;
}

