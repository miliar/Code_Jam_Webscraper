#include<cstdio>
#include<cmath>

using namespace std;
int t;
double c,f,x;

#define eps 1e-8

double func(double c,double f,double x){
    double speed=2,ret=0;
    while(true){
        double t1=x/speed;
        double t2=c/speed+x/(speed+f);
        if(t1<t2){
            ret+=t1;
            break;
        }
        else{
            ret+=c/speed;
            speed+=f;
        }
    }
    return ret;
}


int main(){
    scanf("%d",&t);
    int cas=1;
    while(t--){
        scanf("%lf %lf %lf",&c,&f,&x);
        printf("Case #%d: %.7lf\n",cas++,func(c,f,x));
    }
    return 0;
}
