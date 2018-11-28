#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int t;
    cin >> t;

    double *time = new double[t];

    for (int i = 0; i < t; i++)
    {
        double c, f, x;
        double r = 2;

        cin >> c >> f >> x;

        time[i] = 0;

        while(1)
        {
            if (x / r < ((c / r) + (x / (r + f))))
            {
                time[i] += (x / r);
                break;
            }
            time[i] += (c / r);
            r += f;
        }
    }

    for (int i = 0; i < t; i++)
        cout << "Case #" << (i+1) << ": " << std::setprecision(15) << time[i] << endl;

    delete[] time;
    return 0;
}
