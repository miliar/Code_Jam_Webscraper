#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        const double R = 2.0; // default production rate
        
        double C, F, X; // cost of farm, production rate per farm, production goal
        cin >> C >> F >> X;

        double A = 0.0; // accumulated time
        double B = numeric_limits<double>::max(); // best time
        int Fheld = 0; // farms held

        while (true)
        {
            const double P = R + Fheld * F; // production rate
            double tX = X / P; // time remaining to X

            if (B < A + tX)
            {
                break;
            }

            B = A + tX;
            A += C / P;
            ++Fheld;
        }

        cout << "Case #" << t << " " << fixed << setprecision(7) << B << endl;
    }
    
    return 0;
}
