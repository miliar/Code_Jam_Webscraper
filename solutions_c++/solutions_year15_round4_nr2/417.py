#include <iostream>
#include <set>
#include <iomanip>
#include <cmath>

using namespace std;
double EPSILON = 1E-8;

bool AreEqual(double a, double b)
{
    return fabs(a - b) < EPSILON;
}

void OutputNum(double num)
{
    cout << setprecision(8) << fixed << num << '\n';
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        int N;
        cin >> N;
        
        double neededTemp, neededVolume;
        cin >> neededVolume >> neededTemp;
        
        cout << "Case #" << t << ": ";
        
        if (N == 1)
        {
            // WORKS
            double temp, flow;
            cin >> flow >> temp;
            
            if (AreEqual(temp, neededTemp))
                OutputNum(neededVolume / flow);
            else
                cout << "IMPOSSIBLE\n";
        }
        else
        {
            double temp1, temp2;
            double flow1, flow2;
            cin >> flow1 >> temp1 >> flow2 >> temp2;
            
            if (AreEqual(temp1, temp2))
            {
                if (AreEqual(temp1, neededTemp))
                    OutputNum(neededVolume / (flow1 + flow2));
                else
                    cout << "IMPOSSIBLE\n";
            }
            else
            {
                double v1 = neededVolume * (neededTemp - temp2) / (temp1 - temp2);
                double v2 = neededVolume - v1;
                if (v1 < 0 || v2 < 0)
                {
                    if (AreEqual(temp1, neededTemp))
                        OutputNum(neededVolume / flow1);
                    else if (AreEqual(temp2, neededTemp))
                        OutputNum(neededVolume / flow2);
                    else
                    {
                        cout << "IMPOSSIBLE\n";
                    }
                }
                else
                {
                    OutputNum(fmax(v1 / flow1, v2 / flow2));
                }
            }
        }
    }
}