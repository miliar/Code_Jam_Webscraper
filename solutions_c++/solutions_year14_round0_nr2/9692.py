#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <iomanip>
#include <climits>
#include <limits>

typedef std::numeric_limits<double> dbl;

using namespace std;

double findUpgradeTime(int numUpgrades, double C, double F, double X){
    double t = 0.0;
    int upgradeCount = 0;
    double frequency = 2.0;

    while(upgradeCount < numUpgrades){
        t += C / frequency;
        frequency += F;
        upgradeCount++;
    }

    t += X / frequency;
    return t;
}

double findBestTime(double C, double F, double X){
    //int numUpgrades = (int)(X / F) + 1;
    int numUpgrades = X;
    double minTime = INT_MAX;
    for(int i = 0; i < numUpgrades; ++i){
        double t = findUpgradeTime(i, C, F, X);
        if(t < minTime){
            minTime = t;
        }
    }

    return minTime;
}

int main(int argc, char** argv){
    ofstream outfile;
    outfile.open("output.txt");

    ifstream infile("input.txt");
    string line;


    getline(infile, line);
    int t = atoi(line.c_str());

    // for each test case
    for(int i = 0; i < t; ++i){
        double X, C, F;

        getline(infile, line);
        if(line.length() == 0) continue;
        sscanf(const_cast<char*>(line.c_str()), "%lf %lf %lf", &C, &F, &X);

        double bestTime = findBestTime(C, F, X);

        outfile.precision(dbl::digits10);
        outfile << "Case #" << i + 1 << ": " << bestTime << endl;
    }

    outfile.close();
    return 0;
}