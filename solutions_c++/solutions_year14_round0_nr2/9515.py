#include<stdio.h>
#include<cstdlib>
double solve(double c,double f,double x,double cur){
    if(x/cur<c/cur+x/(cur+f)){
        return x/cur;
    }
    return solve(c,f,x,cur+f)+c/cur;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    
    int cases;
    double c,f,x;
    double time;
    scanf("%d",&cases);
    for(int ca=1;ca<=cases;ca++){
        scanf("%lf%lf%lf",&c,&f,&x);
        time=0;
        printf("Case #%d: %.7lf\n",ca,solve(c,f,x,2.0f));
    }
} 
