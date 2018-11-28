#include <fstream>
#include <string>

using namespace std;

const int MAXT = 100 + 10;
const int MAXN = 100 + 10;
int T, N;
string S;

int GetAns (string s, int n)
{
    int finpos = -1;
    for (int i = 0; i < n; i++)
        if (s[i] == '-')
            finpos = i;
    if (finpos == -1)
        return 0;
    if (finpos == 0)
        return 1;
    for (int i = 0; i < finpos; i++)
        if (s[i] == '+')
            s[i] = '-';
        else if (s[i] == '-')
            s[i] = '+';
    return 1 + GetAns(s, finpos);
}

int main()
{
    ifstream cin("input.in");
    ofstream cout("output.out");
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> S;
        N = S.length();
        cout << "Case #" << t << ": " << GetAns(S, N) << '\n';
    }
    return 0;
}
