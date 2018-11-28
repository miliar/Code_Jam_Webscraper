#include <fstream>
#include <iostream>
#include <ctime>
#include <cstring>
#include <cstdlib>
#define eps 1e-6

using namespace std;

void checkMin(double& x,double y) {
    if (x > y + eps) {
        x = y;
    }
}

void generateData() {
    ofstream cout("B.in");
    srand(static_cast<unsigned int>(time(0)));
    cout << 100 << "\n";
    for (int i = 1; i <= 100; i++) {
        double C = (rand() % 100000 + 1) + (rand() % 100000 + 1) / 100000.0;
        double F = (rand() % 100 + 1) + (rand() % 100000 + 1) / 100000.0; 
        double X =  (rand() % 100000 + 1) + (rand() % 100000 + 1) / 100000.0; 
        cout.precision(7);
        cout << fixed << C << " " << F << " " << X << "\n";
    }

}

int main()
{
    ifstream cin("B.in");
    ofstream cout("B.out");
    int T;
    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        double C, F, X;
        cin >> C >> F >> X;
        double res = X / 2.0; 
        double fs = 0.0;
        for (int k = 1; k <= 20000000; k++) {;
            fs += C / (2.0 + (k - 1) * F);
            checkMin(res,fs + X / (2.0 + k * F));
        }
        
        cout.precision(7);
        cout << "Case #" << testCase << ": ";
        cout << fixed << res << "\n";
    }
    return 0;
}
