#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    ifstream input;
    input.open("input.txt");
    ofstream output;
    output.open("output.txt");
    output << setprecision(20);
    int T;
    input >> T;
        for (int i = 0; i < T; i++){
        double farmcost = 0;
        double cookieimprovement = 0;
        double cookietarget = 0;
        input >> farmcost;
        input >> cookieimprovement;
        input >> cookietarget;
        double cookierate = 2;
        double timepassed = 0;
            while (true){
                if ((cookietarget)/(cookierate) <= ((farmcost/cookierate) + (cookietarget)/(cookierate + cookieimprovement))){
                timepassed = timepassed + (cookietarget)/(cookierate);
                break;
                } else {
                timepassed = timepassed + (farmcost/cookierate);
                cookierate = cookierate + cookieimprovement;
                }
            }
        output << "Case #" << i+1 << ": " << timepassed << endl;
        }
    return 0;
}
