#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int TESTS;
    cin >> TESTS;
    for (int TEST = 1; TEST <= TESTS; TEST++)
    {
        cout << "Case #" << TEST << ": ";
        int n;
        cin >> n;
        vector<int> V(n);
        for (auto & x : V)
            cin >> x;
        int R = *max_element(V.begin(), V.end()), ans = R;
        for (int i = 2; i < R; i++)
        {
            int num = 0;
            for (auto x : V)
                num += (x + i - 1) / i - 1;
            ans = min(ans, num + i);
        }
        cout << ans << '\n';
    }
}

