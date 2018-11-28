#include<cstdio>
int T,n;
double c,f,x,ac,sum,r;
int main(){
    scanf("%d",&T);
    for (int o=1; o<=T; o++){
        scanf("%lf%lf%lf",&c,&f,&x);
        ac=x; sum=0;
        n=0; r=0;
        while (n<=x*10){
            if (sum+x/(r+2)<=ac) ac=sum+x/(r+2);
            sum+=c/(r+2); r+=f;
            ++n;    
        }
        printf("Case #%d: %.7lf\n",o,ac);
    }
    return 0;    
}
