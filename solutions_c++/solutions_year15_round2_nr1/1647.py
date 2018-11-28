#include <bits/stdc++.h>
using namespace std;

const int MAX_SIZE = 1000001;
int arr[MAX_SIZE];

int getReverse(int N)
{
    int result = 0;

    while (N)
    {
        result = (result * 10) + (N % 10);
        N /= 10;
    }

    return result;
}

void solve()
{
    memset(arr, 0x3F, sizeof arr);
    arr[1] = 1;
    for (int i = 1; i < 1000000; ++i)
    {
        int rev = getReverse(i);
        arr[i + 1] = min(arr[i + 1], arr[i] + 1);
        arr[rev] = min(arr[rev], arr[i] + 1);
    }
}

int main()
{
    freopen("A-input.txt", "r", stdin);
    freopen("A-output.txt", "w", stdout);
    int T, N;
    cin >> T;
    solve();

    for (int t = 1; t <= T; t++)
    {
        cin >> N;
        int result = arr[N];
        cout << "Case #" << t << ": " << result << "\n";
    }

    return 0;
}
