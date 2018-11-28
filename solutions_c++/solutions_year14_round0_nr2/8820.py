#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int caseNumber;
    int caseIndex=1;
    freopen("B-large", "r", stdin);
    freopen("output.txt", "w", stdout);
    cout << setprecision(7) << fixed;
    
    scanf("%d", &caseNumber);    
    while(caseIndex<=caseNumber){

        double C, F, X;
        scanf("%lf", &C);
        scanf("%lf", &F);
        scanf("%lf", &X);
        
        // TODO: X<=C
        
        int farmNumber=0;
        double curSum = farmNumber*C;
        double tWaste = 0.00;
        double rate = 2;
        double minTime = X/rate;
        curSum +=C;
        
        while(curSum < X){
            
            double tNotBuild = tWaste + X/(2+farmNumber*F);
            if(tNotBuild<minTime){
                minTime = tNotBuild;
            }
            farmNumber++;
            tWaste += C/rate;
            rate = rate + F;
            curSum = farmNumber*C;
        }
        
        cout << "Case #" << caseIndex << ": " << minTime << endl;
        caseIndex++;
    }
    
   
    return 0;
}

