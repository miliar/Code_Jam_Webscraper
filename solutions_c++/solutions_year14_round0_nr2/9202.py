#include<iostream>
#include<cstdio>
#include<cstring>
#include<set>
using namespace std;
int a[10][10];
int b[10][10];
bool vis[200];
int main(){
    int T,cas = 1;
    freopen("22.in","r",stdin);
    freopen("2.out","w",stdout);
    cin>>T;
    while(T--){
        double C,F,X;
        cin>>C>>F>>X;
        double ans;
        double now = 2.0;
        double t = C / now;
        printf("Case #%d: ",cas++);
        if(X / now <= t){
            ans = X / now;
            printf("%.7f\n",ans);
            continue;
        }
        ans = t;

        while(true){
            double t1 = X / (now + F);
            double t2 = (X - C)/now;
            if(t1 < t2){
                now += F;
            }else{
                ans += t2;
                break;
            }
            ans += C / now;
        }
        printf("%.7f\n",ans);
    }
    return 0;
}
