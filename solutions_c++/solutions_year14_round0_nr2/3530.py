#include<iostream>
#include<cstdio>

using namespace std;

int main() {
    int T;
    double C,F,X, time=0.0, cookieRate = 2.0,totalTime = 0.0; double noOfCookies=0.0;

    freopen("B-large.in", "r", stdin);
    freopen("2.out", "w", stdout);

    cin>>T;
    for(int k = 1 ; k <= T ; k++) {

        totalTime = 0.0;
        noOfCookies=0.0;
        cookieRate = 2.0;
        cin>>C>>F>>X;
        while(noOfCookies < X) {
            time = 0,0;
            if(X<C) {
                time = X/cookieRate;
                noOfCookies = X;
            } else {
                if(noOfCookies < C) {
                    time = (C-noOfCookies)/cookieRate;
                    noOfCookies = C;
                }
                    if((X-noOfCookies + C)/(cookieRate+F) < ((X-noOfCookies)/cookieRate)) {
                        cookieRate += F;
                        noOfCookies -= C;

                    } else {
                        time += (X-noOfCookies)/cookieRate;
                        noOfCookies = X;
                    }
            }
            totalTime += time;
        }
       printf("Case #%d: %.7lf\n",k,totalTime);
    }
    return 0;
}
