#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int solve()
{
    int n, i, ans;
    cin >> n;
    vector<int> A(n);
    for (i = 0; i < n; ++i)
        cin >> A[i];
    ans = 0;
    while(A.size() > 1)
    {
        int m, idx;
        m = A[0];
        idx = 0;
        for (i = 1; i < A.size(); ++i)
            if (A[i] < m)
            {
                m = A[i];
                idx = i;
            }
        if (idx < A.size() - 1 - idx)
            ans += idx;
        else
            ans += A.size() - 1 - idx;
        A.erase(A.begin() + idx);
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


