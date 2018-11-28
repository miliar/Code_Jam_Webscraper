#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        int d;
        cin >> d;

        vector<int> p(d, 0);
        for (int i = 0; i < d; ++i) cin >> p[i];

        int max = 0;
        for (int i = 0; i < d; ++i) if (p[i] > max) max = p[i];

        int best = max;
        for (int lim = 1; lim <= max; ++lim)
        {
            int sum = 0;
            for (int i = 0; i < d; ++i)
            {
                sum += (p[i] - 1) / lim;
            }
            if (sum + lim < best) best = sum + lim;
        }

        cout << "Case #" << i + 1 << ": " << best << endl;
    }

    return 0;
}
