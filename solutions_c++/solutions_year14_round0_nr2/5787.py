#include<stdio.h>
#include<cstdlib>
long a,b,i,j,k,t;
double c,f,x,pa,act,sig,res;
double prod(double p,double c){
    double a;
    a=c/p;
    return a;
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%ld",&t);
    for(int w=1;w<=t;w++){
        pa=2;
        scanf("%lf%lf%lf",&c,&f,&x);
        act=x/pa;
        sig=prod(pa,c)+x/(f+pa);
        pa+=f;
        res=act;
        while(act>sig){
            act=sig;
            sig=act-x/pa;
            sig+=prod(pa,c)+x/(pa+f);
            pa+=f;
            res=act;
        }
        printf("Case #%d: %.7lf\n",w,res);
    }
}
