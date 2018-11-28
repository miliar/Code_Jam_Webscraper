#include <iostream>
#include <iomanip>

using namespace std;

int main(void){
    int numOfCases, i;
    long double totalCookieProduction, possibleCookieProduction;
    long double farmCost, extraCookiesPerFarm, goal;
    long double totalTime, timeIfyouWait, timeToBuyAnotherFarm, possibleTime;
    bool goalReached;
    cin >> numOfCases;
    for(i=1; i<=numOfCases; i++){
        totalCookieProduction = 2;
        totalTime = 0;
        goalReached = false;
        cin >> farmCost;
        cin >> extraCookiesPerFarm;
        cin >> goal;
        while(!goalReached){
            timeIfyouWait = goal/totalCookieProduction;
            timeToBuyAnotherFarm = farmCost/totalCookieProduction;
            possibleCookieProduction = totalCookieProduction+extraCookiesPerFarm;
            possibleTime = timeToBuyAnotherFarm + goal/possibleCookieProduction;
            if(timeIfyouWait<=possibleTime){
                //wait until you have the cookies necessaries
                totalTime += timeIfyouWait;
                goalReached = true;
            }
            else{
                //buy another farm
                totalCookieProduction = possibleCookieProduction;
                totalTime += timeToBuyAnotherFarm;
            }
        }
        cout << "Case #" << i << ": " << setprecision(10) << totalTime << endl;
    }
    return 0;
}
