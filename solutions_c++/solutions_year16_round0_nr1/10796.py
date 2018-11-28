#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("test.txt", "r", stdin);
    freopen("testout.txt","w", stdout);
    long long T, N, ns, bs, answer;
    cin >> T;
    vector <long long> A(10);
    vector <long long> B(T);
    for (long long i = 0; i < T; ++i)
        cin >> B[i];
    for (long long i = 0; i < 10; ++i)
        A[i] = 0;
    for (long long i = 0; i < T; ++i)
    {
        if (B[i] == 0)
            cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
        else
        {
            for (long long j = 1; j < 9223372036854775806; ++j)
            {
                ns = B[i] * j;
                answer = ns;
                while (ns > 0)
                {
                    bs = ns % 10;
                    ns = ns / 10;
                    A[bs] = 1;
                }
                if (A[0] + A[1] + A[2] + A[3] + A[4] + A[5] + A[6] + A[7] + A[8] + A[9] == 10)
                    break;
            }
            cout << "Case #" << i + 1 << ": " << answer << endl;
            for (long long i = 0; i < 10; ++i)
                A[i] = 0;
        }
    }
}
