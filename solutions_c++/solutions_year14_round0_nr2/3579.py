#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;

double C, F, X;
double ans;

int main(){
    int T; cin >> T;
    int k = 0;
    while (T --){
        ++k;
        cin >> C >> F >> X;
        ans = 0;
        bool flag = 0;
        double f = 2; // current magic

        while (! flag){
            double t1 = X / f;
            double t2 = C / f + X / (f + F);
            if (t1 < t2){
                flag = true;
                ans = ans + X / f;
            }
            else{
                ans = ans + C / f;
                f = f + F;
            }
        }

        printf("Case #%d: %.7f\n",k, ans);

   }
}

