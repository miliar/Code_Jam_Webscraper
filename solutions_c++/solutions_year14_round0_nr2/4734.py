#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
double C,F,X,p;
double ans;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T; cin>>T;
    for (int tt=1;tt<=T;tt++){
        printf("Case #%d: ",tt);
        scanf("%lf%lf%lf",&C,&F,&X);
        ans=0; p=2;
        while (true){
            if (C/p+X/(p+F)>X/p){
                ans+=X/p;
                break;
            } else {
                ans+=C/p;
                p+=F;
            }
        }
        printf("%.7lf\n",ans);
    }
}
