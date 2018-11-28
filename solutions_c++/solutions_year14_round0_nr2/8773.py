#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
using namespace std;
int T;
double C,F,X;
double ans, now, pro;
int main(){
    scanf("%d", &T);
    for(int f=1;f<=T;f++){
        scanf("%lf%lf%lf",&C,&F,&X);
        ans = 1e+100;
        now = 0.0;
        pro = 2.0;
        for(int i=0;;i++){
            if( now > ans ){
                break;
            }            
            if( ans > now + X/pro ){
                ans = now + X/pro;
            }
            now += C / pro;
            pro += F;
        }

        printf("Case #%d: %.7lf\n", f, ans);
    }

    return 0;
}
