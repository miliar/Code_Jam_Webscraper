#include <fstream>
#include <iostream>
#include <iomanip>

using std::ifstream;
using std::ofstream;
using std::cout;
using std::endl;
using std::setprecision;
using std::fixed;

double minimumSeconds(double farmCost, double farmFactor, double winValue);
double timeToWin(double winValue, double farmFactor, int numFarms);
double timeToNextFarm(double farmCost, double farmFactor, int numFarms);

const int base_rate = 2;

int main(int argc, char* argv[]){
    if (argc != 3){
        cout << "usage: " << argv[0] << " INPUT_FILE OUTPUT_FILE" << endl;
        return -1;
    }

    ofstream outputFile(argv[2]);
    ifstream inputFile(argv[1]);

    int numCases = 0;
    inputFile >> numCases;

    outputFile << fixed << setprecision(7);
    for (int i = 1; i <= numCases; i++){
        double C, F, X;
        inputFile >> C >> F >> X;
        outputFile << "Case #" << i << ": " << minimumSeconds(C, F, X) << endl;
    }

    return 0;
}

double minimumSeconds(double farmCost, double farmFactor, double winValue){
    int numFarms = 0;
    double totalTime = 0.0;

    double currentLowest = timeToWin(winValue, farmFactor, numFarms);
    double nextFarmIn = timeToNextFarm(farmCost, farmFactor, numFarms);
    double next = timeToWin(winValue, farmFactor, numFarms + 1);

    while (currentLowest >= nextFarmIn + next) {
        totalTime += nextFarmIn;
        numFarms += 1;
        currentLowest = next;
        nextFarmIn = timeToNextFarm(farmCost, farmFactor, numFarms);
        next = timeToWin(winValue, farmFactor, numFarms + 1);
    }

    return totalTime + currentLowest;
}

double timeToWin(double winValue, double farmFactor, int numFarms){
    return winValue / (farmFactor * numFarms + base_rate);
}

double timeToNextFarm(double farmCost, double farmFactor, int numFarms){
    return farmCost / (farmFactor * numFarms + base_rate);
}
