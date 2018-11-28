#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>

#define int64 long long
#define sz(A) (int((A).size()))

using namespace std;

int main()
{
#ifdef shaoling
    freopen("D-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    int T;
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        int n;
        cin >> n;
        vector <double> A(n), B(n);

        for (int i = 0; i < n; i++)
            cin >> A[i];
        sort(A.begin(), A.end());

        for (int i = 0; i < n; i++)
            cin >> B[i];
        sort(B.begin(), B.end());
        int res1 = 0, res2 = 0, ptr = n - 1;

        for (int i = n - 1; i >= 0; i--)
        {
            if (A[ptr] > B[i])
                res1++, ptr--;
        }
        ptr = 0;

        for (int i = 0; i < n; i++)
        {
            while (ptr < n && B[ptr] < A[i])
                ptr++;

            if (ptr == n)
                res2++;
            else
                ptr++;
        }
        cout << "Case #" << t + 1 << ": " << res1 << ' ' << res2 << '\n';
    }
    return 0;
}