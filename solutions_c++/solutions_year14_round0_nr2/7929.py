#include <iostream>

double timeToReachTarget(double productionRate, double target) {
    return target / productionRate;
}

void processCase(int caseNumber) {
    double farmCost, farmProductionRate, targetNumberOfCookies;
    std::cin >> farmCost >> farmProductionRate >> targetNumberOfCookies;
    
    double initialProductionRate = 2.0;
    double bestTime = timeToReachTarget(initialProductionRate, targetNumberOfCookies);
    
    int numberOfFarms = 0;
    double buildTime = 0.0;
    bool finished = false;
    
    while (!finished) {
        buildTime += timeToReachTarget(initialProductionRate + numberOfFarms * farmProductionRate, farmCost);
        numberOfFarms++;
        double cookiesTime = timeToReachTarget(initialProductionRate + numberOfFarms * farmProductionRate, targetNumberOfCookies);
        double totalTime = buildTime + cookiesTime;
        
        if (totalTime < bestTime) {
            bestTime = totalTime;
        }
        else {
            finished = true;
        }
    }
    
    std::cout.precision(7);
    std::cout << "Case #" << caseNumber << ": " << std::fixed << bestTime << std::endl;
}

int main() {
    int numberOfCases;
    std::cin >> numberOfCases;
    
    for (int i = 1; i <= numberOfCases; i++) {
        processCase(i);
    }
    
    return 0;
}

