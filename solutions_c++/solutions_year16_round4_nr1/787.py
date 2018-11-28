#include<iostream>
#include<vector>
#include<sstream>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

bool play(string & S)
{
    string R;
    for (int i = 0; i < S.size(); i += 2)
    {
        if      (S[i] == 'P' && S[i + 1] == 'R')
            R += 'P';
        else if (S[i] == 'R' && S[i + 1] == 'P')
            R += 'P';
        else if (S[i] == 'R' && S[i + 1] == 'S')
            R += 'R';
        else if (S[i] == 'S' && S[i + 1] == 'R')
            R += 'R';
        else if (S[i] == 'S' && S[i + 1] == 'P')
            R += 'S';
        else if (S[i] == 'P' && S[i + 1] == 'S')
            R += 'S';
        else
            return false;
    }
    S = R;
    return true;
}

bool check(string S)
{
    while (S.size() != 1)
        if (play(S) == false)
            return false;
    return true;
}

string solve()
{
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    string S = string(p, 'P') + string(r, 'R') + string (s, 'S');
    if (check(S))
        return S;
    while(next_permutation(S.begin(), S.end()))
        if (check(S))
            return S;
    return "IMPOSSIBLE";
}

int main()
{
    int T, t;
    cin >> T;
    for (t = 1; t <= T; ++t)
    {
        cout << "Case #" << t << ": " << solve() << endl;
    }
    return 0;
}

