#include <iostream>

int main(int argc, const char * argv[])
{
    std::cout.precision(8);
    std::cout.setf(std::ios::fixed);
    
    int numberOfTestCases;
    
    std::cin >> numberOfTestCases;
    
    for(int line = 0; line < numberOfTestCases; line++) {
        
        double cps = 2.0;
        double farmCost;     // C
        double cpsIncrese;   // F
        double cookiesToWin; // X
        
        std::cin >> farmCost >> cpsIncrese >> cookiesToWin;
        
        bool shouldBuyFarm;
        double totalTime = 0.0;
        do {
            double timeToWin = cookiesToWin / cps;
            double timeToWinIfBuyFarm = cookiesToWin / (cps+cpsIncrese);
            double timeToFarm = farmCost / cps;
            
            double savingsForBuyingFarm = timeToWin - timeToWinIfBuyFarm;
            
            shouldBuyFarm = savingsForBuyingFarm > (farmCost/cps);
            if(shouldBuyFarm) {
                totalTime += timeToFarm;
                cps += cpsIncrese;
                
            } else {
                totalTime += timeToWin;
            }
            
        } while (shouldBuyFarm);
        
        std::cout << "Case #" << (line+1) << ": " << totalTime << std::endl;
        
    }
    
    return 0;
}