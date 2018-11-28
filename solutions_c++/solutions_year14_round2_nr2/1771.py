#include <algorithm>
#include <iostream>

using namespace std;

void solve()
{
    int A, B, K;
    cin >> A >> B >> K;

    int count = 0;
    for (int a = 0; a < A; a++)
    {
        for (int b = 0; b < B; b++)
        {
            if ((a & b) < K)
            {
                count++;
            }
        }
    }
    cout << count << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

