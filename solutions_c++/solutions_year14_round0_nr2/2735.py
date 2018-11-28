#include<cstdio>
int main(){
    int N;
    scanf("%d",&N);
    for(int i=0;i<N;i++){
            double C,F,X;
            double aux=2.0;
            double rec=0;
            scanf("%lf %lf %lf",&C,&F,&X);
            double menor=X/aux; 
            while(1){       
                rec+=C/aux;
                aux+=F;
                if(menor>rec+(X/(aux))){
                   menor=rec+(X/(aux)); 
                }
                else break;
            }
            printf("Case #%d: %.7lf\n",i+1,menor);
    }    
    
}
