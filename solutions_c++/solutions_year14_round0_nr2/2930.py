#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

double solveB(double time, double C, double F, double X, double R);

int main() {
    string test_filename;
    cout << "Enter test file : " << endl;
    getline(cin, test_filename);
    cout << endl;

    string out_name = test_filename.substr(0, test_filename.find_last_of(".")) + ".out";
    ifstream in_file(test_filename.c_str());
    ofstream out_file(out_name);

    int T;
    in_file >> T;

    for(int t = 0; t < T; t++) {
        double C, X, F;
        in_file >> C >> F >> X;
        
        double best = solveB(0, C, F, X, 2);


        out_file << "Case #" << t + 1 << ": " << std::fixed << std::setprecision(9) << best << endl;

    }
    out_file.close();
}

double solveB(double time, double C, double F, double X, double R) {

    double time_if_wait = X/R;

    double time_to_get_farm = C/R;

    double time_after_farm = X/(R + F);

    if(time_if_wait < time_to_get_farm + time_after_farm) {
        return time + time_if_wait;
    }
    else {
        return solveB(time + time_to_get_farm, C, F, X, R + F);
    }
}
