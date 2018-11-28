#include<stdio.h>
//#include<conio.h>
double func(double,double,double,double);
int main(){
    freopen("C:\\A\\input.txt","r",stdin);freopen("C:\\A\\output.txt","w",stdout);freopen("C:\\A\\err.txt","w",stderr);
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
            double rate=2.0;
            double C,F,X;
            scanf("%lf%lf%lf",&C,&F,&X);
            //printf("before %f\n");
            double time= func(C,F,X,rate);
            printf("Case #%d: %.7lf\n",i+1,time);
                 }
                 return 0;
                 }
                 
double func(double c, double f, double x, double rate){
           double time;
           double currate;
           double newtime;
           double minx;
           if(c>=x){ time=x/rate; return time;}
           time=c/rate;
          // printf("after@1 %lf\n",time);
           if(c/rate+x/(rate+f) >= x/rate){  return x/rate;}
           minx=x-c;
           currate = rate+f;
          // printf("after@1 %f\n",time);
           newtime = time + func(c,f,x,currate);
           time=time+minx/rate;
           //printf("after@2 %f\n",time);
           if(time<=newtime){ return time;}
           else{ return newtime;}
           }
