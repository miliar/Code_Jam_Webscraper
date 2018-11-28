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
    int t;
    input >> t;
    double gain;
    double currenttime;
    for (int i = 0; i < t; i++) {
        gain = 2;
        currenttime = 0;
        double c, f, x;
        input >> c >> f >> x;
        while (true) {
            //compare time waiting to time to buy a farm then wait
            double time1 = (x)/gain;
            double time2 = (c)/gain + (x)/(gain + f);
            if (time1 <= time2) { //we done
                output << "Case #" << i + 1 << ": " << time1 + currenttime << endl;
                break;
            } else { //not done, but buy a farm
                currenttime = currenttime + (c)/gain;
                gain = gain + f;
            }
        }
    }
    return 0;
}
