#include <stdio.h>
void func(double g,double c,double f,double x,double b,int i){
    if(x/b<=c/b+x/(b+f)){
        printf("Case #%d: %.7lf\n",i+1,g+x/b);
        return;
    }
    g+=c/b;
    b+=f;
    func(g,c,f,x,b,i);
}
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out2.txt","w",stdout);
    double g,c,x,f,b=2;
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%lf %lf %lf",&c,&f,&x);
        func(0,c,f,x,b,i);
    }
    return 0;
}
