#include <stdio.h>

int main()
{
    int caseNum;
    scanf("%d", &caseNum);

    int caseCounter = 1;
    while(1){
        if(caseCounter>caseNum) break;
        double farmCost, farmEarn, goal;
        
        // input stage
        scanf("%lf %lf %lf", &farmCost, &farmEarn, &goal);

        // processing stage
        double ans = 0.0, rate = 2.0;
        while(1){
            double secToBuyFarm = farmCost/rate;
            double ansIfNotBuy = goal/rate;
            double ansIfBuy = secToBuyFarm + goal/(rate+farmEarn);
            if(ansIfBuy < ansIfNotBuy){
                ans += secToBuyFarm;
                rate += farmEarn;
            } else {
                ans += ansIfNotBuy;
                break;
            }
        }

        // output stage
        printf("Case #%d: ", caseCounter);
        printf("%.7f\n", ans);

        caseCounter++;
    }

    return 0;
}
