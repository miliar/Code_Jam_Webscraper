#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <stack>
#include <iomanip>      // std::setprecision

using namespace std;

int main(int argc, char* args[]) {
        // Open the file
    ifstream ifs("B-large.in");
    ofstream ofs("output.txt");

    string line;
    getline(ifs, line);
    stringstream ssNum(line);
    int num;
    ssNum >> num;

    

    for (int i = 0; i < num; i++) {
        getline(ifs, line);
        stringstream ss(line);
        double C;
        ss >> C;
        double F;
        ss >> F;
        double X;
        ss >> X;

        double f = 2;
        double x = X;

        double answer = 0;

        double secsToReach = X / f;
        while (true) {
            double secsToReach = X / f;
            double secsToBuyFarm = C / f;
            double secsToReachAfterBuyFarm = X / (f + F);

            if (secsToBuyFarm + secsToReachAfterBuyFarm < secsToReach) {
                answer += secsToBuyFarm;
                f += F;
            } else {
                answer += secsToReach;
                break;
            }
        }

        ofs << "Case #" << (i + 1) << ": " << fixed << std::setprecision(7) << answer << endl;
    }

    ifs.close();
    ofs.close();
}
