#include<bits/stdc++.h>

using namespace std;

int main(){
    //freopen("B-large.in", "r", stdin);
    //freopen("BOUTLARGE.txt", "w", stdout);

    int T;
    cin>>T;
    for(int line = 1; line <= T; line++){
        double C, F, X, ans = 0;
        cin>>C>>F>>X;
        double myF = 2;
        while(true){
            double finish = X / myF;
            double factory = C / myF;
            double tempF = myF + F;
            double factoryBoost = X / tempF;
            if(factory + factoryBoost >= finish){
                ans += finish;
                break;
            }
            else{
                ans += factory;
                myF += F;
            }
        }
        printf("Case #%d: %0.7lf\n", line, ans);
    }
    return 0;
}
