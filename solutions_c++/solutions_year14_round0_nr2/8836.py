#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

double findWinTime(double farmCost, double prodInce, double winningNum);
int getNumCases();
double* getGameStats();

ifstream inFile;
int main(int argc, char** argv){
    cout.precision(7);
    string infilename;
    if(argc > 1){
        infilename = argv[1];
    }
    else{
        infilename = "input.txt";
    }
    int numberOfTestCases;
    string line;
    ofstream outFile;
    outFile.precision(7);
    string outfilename = "output.txt";
    outFile.open(outfilename.c_str());
    inFile.open(infilename.c_str());
    if(inFile.is_open()){
        numberOfTestCases = getNumCases();
        cout<<"numberOfTestCases: "<<numberOfTestCases<<"\n";
        for(int i = 0; i < numberOfTestCases; i++){
            double* arr = getGameStats();
            double time = findWinTime(arr[0], arr[1], arr[2]);
            outFile << "Case #"<<i + 1<<": "<<fixed<<time<<"\n";
        }
    }
}

double* getGameStats(){
    string line;
    double* arr = new double[3];
    if(getline(inFile, line)){
        istringstream ss(line);
        for(int column = 0; column < 3; column++){
            if(ss >> arr[column]){
            }
        }
    }
    else{
        cout<<"error in input file\n";
    }
    return arr;
}

   

double findWinTime(double farmCost, double prodInc, double winningNum){
    double CostOfFarm = farmCost;
    double IncreaseInProduction = prodInc;
    double currentProductionRate = 2.0;
    double WinningNumber = winningNum;
    double timeUntilFarm = CostOfFarm/currentProductionRate;
    double timeUntilWin = WinningNumber/currentProductionRate;
    double prevTotalTime;
    double totalFarmBuildingTime = timeUntilFarm;
    double answer;
    double newTime = totalFarmBuildingTime + (WinningNumber/(currentProductionRate + IncreaseInProduction));
    while(newTime < timeUntilWin){
        timeUntilWin = newTime;
        currentProductionRate = currentProductionRate + IncreaseInProduction;
        timeUntilFarm = CostOfFarm/currentProductionRate;
        totalFarmBuildingTime = totalFarmBuildingTime + timeUntilFarm;
        newTime = totalFarmBuildingTime + (WinningNumber/(currentProductionRate + IncreaseInProduction));
    }
    cout.precision(7);
    cout<<"time: "<<fixed<<timeUntilWin;
    return timeUntilWin;
}


int getNumCases(){
    string line;
    int numCases;
    if(getline(inFile, line)){
        istringstream ss(line);
        if(ss >> numCases){
            return numCases;
        }
        else{
        }
    }
    else{
        cout<<"error in input file\n";
    }
    return -1;
}
