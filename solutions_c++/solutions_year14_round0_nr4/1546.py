#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int solve(vector<double> &a, vector<double> &b, int n)
{
    int i = 0, j = 0;
    while (i < n)
    {
        while (j < n && b[j] < a[i])
            ++j;
        if (j == n)
            break;
        ++i;
        ++j;
    }
    return n - i;
}

int main()
{
    int T;
    cin >> T;
    for (int cs = 1; cs <= T; ++cs)
    {
        int n;
        cin >> n;
        vector<double> a, b;
        for (int i = 0; i < n; ++i)
        {
            double t;
            cin >> t;
            a.push_back(t);
        }
        for (int i = 0; i < n; ++i)
        {
            double t;
            cin >> t;
            b.push_back(t);
        }
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());

        cout << "Case #" << cs << ": " << n - solve(b, a, n) << " " << solve(a, b, n) << endl;
    }
    return 0;
}
