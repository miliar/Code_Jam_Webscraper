#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <unordered_map>
#include <queue>
#include <cmath>

using namespace std;

static const string _q = "A";

void gen_strings(int N, string & s1, string & s2, string & s3)
{
    s1 = "P";
    s2 = "R";
    s3 = "S";

    for (int i = 0; i < N; i++)
    {
        string s12, s13, s23;
        s12 = s1 + s2;
        s13 = s1 + s3;
        s23 = s2 + s3;

        s1 = s12;
        s2 = s13;
        s3 = s23;
    }
}

bool is_poss(string & s, int R, int P, int S)
{
    vector<int> ret(3, 0);

    for (int i = 0; i < s.size(); i++)
    {
        if (s[i] == 'P')
            ret[0]++;
        else if (s[i] == 'R')
            ret[1]++;
        else
            ret[2]++;
    }

    return (ret[0] == P && ret[1] == R && ret[2] == S);
}

void solve()
{
    int N, R, P, S; cin >> N >> R >> P >> S;

    string s1, s2, s3;

    gen_strings(N, s1, s2, s3);

    if (is_poss(s1, R, P, S)) cout << s1;
    else if (is_poss(s2, R, P, S)) cout << s2;
    else if (is_poss(s3, R, P, S)) cout << s3;
    else cout << "IMPOSSIBLE";

}

int main(void)
{
    ifstream in(_q + ".in");
    ofstream out(_q + ".out");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());

    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
