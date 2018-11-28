#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main(int argc, char *argv[]) {
    int T = 0;
    cin >> T;
    int n1, n2;
    vector<double> result;
    int temp;
    for (int t=0; t<T; t++) {
        double C, F, X;
        cin >> C >> F >> X;
        double time = .0;
        double rate = 2.0;
        while (1) {
            double noFarmT = X/rate;
            double addFarmT = C/rate + X/(rate+F);
            if (noFarmT <= addFarmT) {
                time += noFarmT;
                break;
            } else {
                //build one farm
                time += C/rate;
                rate += F;
            }
        }
        result.push_back(time);
    }
    cout.precision(7);
    for (int t=0; t<T; t++) {
        cout << "Case #" << t+1 << ": " << std::fixed << result[t] << endl;
    }
}
