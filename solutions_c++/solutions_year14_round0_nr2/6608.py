#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <set>
#include <sstream>

using namespace std;

int main()
{
    //ifstream infile("B-small-attempt0.in");
    ifstream infile("B-large.in");
    //ifstream infile("ProblemBInput.txt");
    ofstream outfile("ProblemBOutputLarge.txt");

    int T;
    infile >> T;

    for (int i = 0; i < T; i++) {
        double rate = 2.0;
        double time = 0.0;
        double C,F,X;
        infile >> C >> F >> X;

        double numToBuy = max(ceil(((X-C)*F/C - rate)/F),0.0);

        for (double j = 0.0; j < numToBuy; j++)
            time += C/(rate + j*F);
        time += X/(rate + numToBuy*F);

        outfile << "Case #" << setprecision(20) << (i+1) << ": " << time << endl;
    }
    return 0;
}
