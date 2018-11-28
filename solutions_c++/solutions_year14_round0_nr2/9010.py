#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

ifstream in("B-large.in");
ofstream out("out_big.txt");

int T;
double C, F, X;

double Farm(int iter)
{
    return (C / (2.0 + static_cast<double>(iter) * F));
}

double resultX(int iter)
{
    return (X / (2.0 + static_cast<double>(iter) * F));
}

double result()
{
    double Z0 = 0.0, Z1 = 0.0;
    double result = 0.0;

    for (int i = 0; ; i++) {
        Z1 += Farm(i); // Z1
        result = resultX(i);

        if (Z0 + result < Z1 + resultX(i+1)) {
            break;
        }
        else {
            Z0 = Z1;
        }
    }

    return (Z0 + result);
}

int main()
{
    in >> T;

    for (int i = 0; i < T; i++) {
        in >> C >> F >> X;

        cout << "Case #" << i+1 << ": " << result() << fixed << setprecision(7) << endl;
        out << "Case #" << i+1 << ": " << result() << fixed << setprecision(7) << endl;
//        cout << C << F << X << endl;
    }

//    cout << T << endl;
    return 0;
}

