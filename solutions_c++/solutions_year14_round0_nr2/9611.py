#include <iostream>
#include <iomanip>

using namespace std;

const double EPS = 1.0E-7;

int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        double C, F, X;
        cin >> C >> F >> X;
        double bestTime = X / 2.0;
        int iterations = 1;

        while (true)
        {
            double time = bestTime;
            time -= (X / (2.0 + (iterations - 1)*F));
            time += (C / (2.0 + (iterations - 1)*F));
            time += (X / (2.0 + (iterations)*F));

            if ((time - bestTime) > EPS)
            {
                break;
            }
            else
            {
                bestTime = time;
                ++iterations;
            }
        }

        cout << "Case #" << t << ": " << fixed << setprecision(7) << bestTime << endl;
    }

    return 0;
}
