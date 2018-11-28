#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        int n;
        int maxp = 0;
        cin >> n;

        vector<int> p(n);
        for (int i = 0; i < n; ++i)
        {
            cin >> p[i];
            maxp = max(maxp, p[i]);
        }
        int result = maxp;
        for (int i = 1; i <= maxp; ++i)
        {
            int t = 0;
            for (int j = 0; j < n; ++j)
            {
                t += p[j] / i;
                if (p[j] % i == 0)
                    --t;
            }
            if (i + t < result)
                result = i + t;
        }
        cout << "Case #" << t << ": " << result << endl; 
    }
}