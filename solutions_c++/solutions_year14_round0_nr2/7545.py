#include <iostream>
#include <stdio.h>

using namespace std;

int main() {
    int NN;
    scanf("%d",&NN);
    for (int II = 0; II < NN; ++II) {
        double c,f,x;
        scanf("%lf %lf %lf", &c,&f,&x);
        double cookiePerSec = 2;
        double totalTime = 0;
        double theBestTime;
        while (1) {
            theBestTime = x/cookiePerSec;
            double challengeBestTime = c/cookiePerSec + x/(cookiePerSec + f);
            //printf("c = %.7lf, x = %.7lf\n", c/cookiePerSec, x/(cookiePerSec + f));
            if (challengeBestTime < theBestTime) {
                //printf("challengeBestTime = %.7lf\n",challengeBestTime);
                totalTime += c/cookiePerSec;
                cookiePerSec += f;
            }
            else {
                //printf("theBestTime = %.7lf\n", theBestTime);
                totalTime += theBestTime;
                break;
            }
        }
        printf("case #%d: %.7lf\n", II+1, totalTime);
    }
}