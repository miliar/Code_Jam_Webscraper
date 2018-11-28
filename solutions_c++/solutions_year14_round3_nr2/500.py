#include <iostream>
#include <vector>
#include <set>
#include <cstdio>
#include <algorithm>
#include <map>

#define sz(A) (int(A.size()))
#define int64 long long

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        int n;
        cin >> n;
        vector <string> A(n);
        vector <int> C(n);

        for (int i = 0; i < n; i++)
        {
            cin >> A[i];
            C[i] = i;
        }
        sort(A.begin(), A.end());
        vector <string> B = A;
        int res = 0;

        do
        {
            for (int i = 0; i < n; i++)
            {
                A[i] = B[C[i]];
            }
            vector <int> bl(200);
            bool good = 1;
            char prev = '-';

            for (int i = 0; i < n && good; i++)
            {
                for (int j = 0; j < sz(A[i]) && good; j++)
                {
                    if (A[i][j] != prev)
                    {
                        if (bl[A[i][j]] == 1)
                            good = 0;
                        bl[A[i][j]] = 1;
                    }
                    prev = A[i][j];
                }
            }

            if (good)
                res++;
        } while (next_permutation(C.begin(), C.end()));
        cout << "Case #" << t + 1 << ": " << res << '\n';
        cerr << t + 1 << '\n';
    }
    return 0;
}
