#include<cstdio>
using namespace std;
double esp=0.0000005;
int main(){
    int t;
    double c,f,x,r,time1,time2,time;
    scanf("%d",&t);
    for(int tc=0;tc<t;tc++){
        scanf("%lf%lf%lf",&c,&f,&x);
        time=0;
        r=2.0;
        while(true){
            time1=c/r+x/(r+f);
            time2=x/r;
            //printf("%lf %lf\n",time1,time2);
            if((long long)(time1*1e10)>(long long)(time2*1e10)) {break;}
      //      if(time1>time2) break;
            time+=c/r;
            r+=f;
        }
        time+=x/r;
        printf("Case #%d: %0.7lf\n",tc+1,time);
    }
    return 0;
}

