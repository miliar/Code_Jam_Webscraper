#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


int solve()
{
    int A[10000];
    int N, i, j, k, ans, X;
    ans = 0;
    cin >> N >> X;
    for (i = 0; i < N; ++i)
    {
        cin >> A[i];
    }
    sort(A, A + N);
    j = N - 1;
    while (j >= 0)
    {
        while (j >= 0 && A[j] == 1000)
            --j;
        if (j < 0)
            break;
        ans += 1;
        k = j - 1;
        while (k >= 0 && A[k] + A[j] > X)
            k--;
        if (k >= 0)
            A[k] = 1000;
        --j;
    }
    return ans;
}

int main()
{
    int T, num;
    cin >> T;
    for (num = 1; num <= T; ++num)
    {
        cout << "Case #" << num << ": " << solve() << endl;
    }
}


