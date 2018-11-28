#include <bits\stdc++.h>

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
        int Smax, ans = 0, now = 0;
        cin >> Smax;
        string S;
        cin >> S;
        for (size_t i = 0; i < S.size(); i++)
        {
            if (now < i)
                ans += i - now, now = i;
            now += S[i] - '0';
        }
        cout << ans << '\n';
    }
}
