#include <iostream>
#include <string>
#include <set>
#include <cmath>
#include <iomanip>

using namespace std;


int main (int argc, char* argv[])
{
    int T = 0;
    string dummy;
    cin >> T;
    getline(cin,dummy);

    for (int i = 0; i < T; ++i)
    {
        double C = 0.0;
        string dummy;
        cin >> C;

        double F = 0;
        cin >> F;

        double X = 0.0;
        cin >> X;
        getline(cin,dummy);


        double b = 2.0; 

        cout << setprecision(10);
        double T = 0;
        double n = X/C - 1.0 - b/F;
        if (C >= X || n <= 0)
        {
            T = X/b;
        }
        else
        {
            int N = ceil(n);
            T = C/b + X/(b+N*F);
            for (int i = 1; i < N; ++i)
            {
                T += C/(b+i*F);
            }
        }
        cout << "Case #" << (i+1) << ": " << T << endl;
    }

    return 0;
}


