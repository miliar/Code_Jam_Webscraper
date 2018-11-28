#include<stdio.h>
main(){
    int T,Case=0;
    double p,c,f,x,num,cnt,ans;
    scanf("%d",&T);
    while(T--){
        cnt=num=0.0;
        p=2;
        scanf("%lf%lf%lf",&c,&f,&x);
        ans=x/2.0;
        while(1){
            double tmp=c/p+x/(p+f)+num;
            num=num+c/p;
            p+=f;
            if(ans>tmp)ans=tmp;
            else break;
        }
        printf("Case #%d: %.7f\n",++Case,ans);
    }
}
