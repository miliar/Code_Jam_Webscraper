#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solve(vector<int>& A)
{
    int ans = 0;
    while (!A.empty())
    {
        int N = (int)A.size();
        vector<int>::iterator it = min_element(A.begin(), A.end());
        int i = it - A.begin();
        ans += min(i, N - 1 - i);
        A.erase(it);
    }
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase)
    {
        int N;
        cin >> N;
        vector<int> A(N);
        for (int i = 0; i < N; ++i)
            cin >> A[i];
        int ans = solve(A);
        cout << "Case #" << testcase << ": " << ans << "\n";
    }
    return 0;
}
