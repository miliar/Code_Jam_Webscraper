#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

double timeToNextFarm(int numFarms, double c, double f) {
    return c / (f * numFarms + 2);
}

double timeReductionOfNextFarm(int numFarms, double x, double f) {
    return (x / (f * numFarms + 2)) - (x / (f * (numFarms + 1) + 2));
}

int main() {
    int numCases;

    ifstream inFile("cookie-clicker.in");
    ofstream outFile("cookie-clicker.out");

    inFile >> numCases;

    for (int i = 0; i < numCases; ++i) {
        double c;
        double f;
        double x;
        int numFarms = 0;
        double timeToWin = 0;

        inFile >> c >> f >> x;

        while (timeToNextFarm(numFarms, c, f) < timeReductionOfNextFarm(numFarms, x, f)) {
            timeToWin += timeToNextFarm(numFarms, c, f);
            numFarms++;
        }

        timeToWin += x / (f * numFarms + 2);

        outFile << fixed << std::setprecision(7);
        outFile << "Case #" << i + 1 << ": " << timeToWin << endl;
    }

    return 0;
}