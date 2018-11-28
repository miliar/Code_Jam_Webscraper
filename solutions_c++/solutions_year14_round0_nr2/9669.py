#include <iostream>
#include <cstdio>
#include <stack>
#include <queue>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>

#define PN(n) printf("%d\n", n)
#define DEBUG if(1)

#define PL(x) printf("Ans: %0.7lf\n", x);

#define LL long long int
#define ULL unsigned long long int

using namespace std;
double C, F, X;

#define DELTA 0.000000001

double timeTaken(int farms){
    double curRate = 2.0;
    int farmsBought = 0;
    double totalTime = 0.0;

    while(farmsBought < farms){
        totalTime += C*1.0/curRate;
        //printf("TotalTime: %lf - F: %lf\n", totalTime, curRate);
        curRate += F;
        farmsBought++;
    }
    totalTime += X*1.0/curRate;
    //printf("Final TotalTime: %lf\n", totalTime);
    return totalTime;
}

int optimal(int n){
    double x, y, z;
    if(n > 0) x = timeTaken(n - 1);
    y = timeTaken(n);
    z = timeTaken(n + 1);

    //printf("N: %d, X: %0.8lf Y: %0.8lf Z: %0.8lf\n", n, x, y, z);

    if(n == 0){
        if(y < z - DELTA){ 
            return 0;
        }
        else return 1;
    }
    else{
        if((y < x + DELTA) && (y < z + DELTA)){
            return 0;
        }
        else if(y > x + DELTA) return -1;
        else if(y > z + DELTA) return 1;
    }
    return 10;
}

double findMin(int u){
    int lower = 0;
    int upper = u;
    int middle;

    /*for(int i = 1; i < 100; i++){
        printf("%d: %d\n", i, optimal(i));
        if(optimal(i) == 0){
            printf("Ans: %0.7lf\n", timeTaken(i));
        }
    }*/

    //printf("--%0.7lf %0.7lf %0.7lf", timeTaken(temp-1), timeTaken(temp), timeTaken(temp+1));

    while(lower < upper){
        //printf("Bin: %d %d\n", lower, upper);
        middle = (lower + upper)/2;

        if(lower == upper - 1){
            if(optimal(lower) == 0){
                //int temp = lower;
                //printf("--%0.7lf %0.7lf %0.7lf\n", timeTaken(temp-1), timeTaken(temp), timeTaken(temp+1));
                return timeTaken(lower);
            }
            else {
                //int temp = upper;
                //printf("--%0.7lf %0.7lf %0.7lf\n", timeTaken(temp-1), timeTaken(temp), timeTaken(temp+1));
                return timeTaken(upper);
            }
        }

        int l = optimal(middle);
        //printf("L: %d\n", optimal(middle));
        if(l == 0){
            //int temp = middle;
            //printf("--%0.7lf %0.7lf %0.7lf\n", timeTaken(temp-1), timeTaken(temp), timeTaken(temp+1));
            return timeTaken(middle);
        }
        else if (l == 1) lower = middle;
        else if (l == -1) upper = middle;
    }

    return timeTaken(1);

}
void run(int caseID){
    int u = 10;
    while(optimal(u) != -1) u *= 2;
    //DEBUG printf("Upper; %d\n", u);
    //DEBUG for(int i = 0; i <= 10; i++) PN(optimal(i));
    /*
    PN(optimal(1932));
    PN(optimal(1933));
    PN(optimal(1934));
    PN(optimal(1936));
    */
    /*
    double min = 99999999;
    for(int i = 0; i < 6000; i++){
        double temp = timeTaken(i);
        if(temp < min) min = temp;
    }
    printf("Case #%d: %0.7lf\n", caseID, min);
    */
    printf("Case #%d: %0.7lf\n", caseID, findMin(u));
}

int main(void) {
    //C = 500.0, F = 4.0, X = 2000.0;
    //C = 30.0, F = 1.0, X = 2.0;
    //run(1);
    int t, T;
    scanf("%d", &T);
    for(t = 1; t <= T; t++){
        scanf("%lf %lf %lf", &C, &F, &X);
        run(t);
    }
    return 0;
}

