#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
#define INF 0x3f3f3f3f
double getTime(int m,double C,double F,double X){
    double rate=2,cookie=0;
    double ans=0;
    while(m--){
        ans+=C/rate;
        rate+=F;
        //printf("%d %.3lf\n",m,rate);
    }
    ans+=X/rate;
    return ans;
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,cas=1;
    scanf(" %d",&T);
    while(T--){
        double C,F,X;
        scanf(" %lf %lf %lf",&C,&F,&X);
        //printf("%.3lf %.3lf %.3lf\n",C,F,X);
        int left=0,right=100010;
        double ans=1e40;
        while(left<=right){
            int m1=(left+right)/2;
            int m2=(m1+right)/2;
            double t1=getTime(m1,C,F,X);
            double t2=getTime(m2,C,F,X);
            if(t1<t2){
                right=m2-1;
            }else{
                left=m1+1;
            }
            ans=min(ans,min(t1,t2));
        }
        for(int i=-10;i<11;i++){
            ans=min(ans,getTime(max(0,left+i),C,F,X));
        }
        printf("Case #%d: %.7lf\n",cas++,ans);
    }
    //system("pause");
    return 0;
}
