#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

double findTimeUntilBuy(double &farmCost, double &cookies, double &cookieRate) {
    double difference;
    difference = farmCost - cookies;
    if(difference > 0) {
        return (difference)/cookieRate;
    } else {
        return 0.0;
    }
}

void findTime(double &farmCost, double &farmAmount, double &targetAmount) {
    double cookieRate = 2.0, cookiesNow = 0.0, cookiesThen = 0.0;
    double timeNoBuy = 0.0, timeUntilBuy = 0.0, timeAfterBuy = 0.0;
    double totalTime = 0.0;

    while(true) {
        timeNoBuy = ((targetAmount - cookiesNow) / cookieRate);
        timeUntilBuy = findTimeUntilBuy(farmCost, cookiesNow, cookieRate);
        cookiesThen = (cookieRate * timeUntilBuy) + cookiesNow;
        timeAfterBuy = ((targetAmount - (cookiesThen - farmCost))/(cookieRate + farmAmount));
        
        if(timeNoBuy < (timeUntilBuy + timeAfterBuy)) {
            totalTime += timeNoBuy;
            break;
        } else {
            totalTime += timeUntilBuy;
            cookiesNow -= cookiesThen - farmCost;
            cookieRate += farmAmount;
        }
    }
    printf("%.7f\n", totalTime);
}

int main() {
    int i;
    int T;
    double farmCost = 0.0, farmAmount = 0.0, targetAmount = 0.0;
    
    ifstream testFile("b.in");
    freopen("b.out", "w", stdout);
    
    testFile >> T;
    
    for(i = 0; i < T; i++) {
        testFile >> farmCost;
        testFile >> farmAmount;
        testFile >> targetAmount;
        cout << "Case #" << i+1 << ": ";
        findTime(farmCost, farmAmount, targetAmount);
    }
}
