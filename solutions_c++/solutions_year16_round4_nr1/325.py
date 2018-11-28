//Problem A. Rather Perplexing Showdown
//By: phoenixinter@gmail.com
//May 28, 2016

#include <iostream>
#include <string>
using namespace std;

int nR, nP, nS;

string dfs(int currDepth, int maxDepth, string ans)
{
    if (currDepth == maxDepth)
        return ans;
    else
    {
        string sr = dfs(currDepth, maxDepth - 1, "R");
        string sp = dfs(currDepth, maxDepth - 1, "P");
        string ss = dfs(currDepth, maxDepth - 1, "S");
        if (ans == "R") return sr < ss ? sr + ss : ss + sr;
        else if (ans == "P") return sp < sr ? sp + sr : sr + sp;
        else return ss < sp ? ss + sp : sp + ss;
    }
}

bool valid(string str, int r, int p, int s)
{
    int nr = 0, np = 0, ns = 0;
    for (int i = 0; i < str.size(); i++)
    {
        if (str[i] == 'R') nr++;
        else if (str[i] == 'P') np++;
        else ns++;
    }
    return nr == r && np == p && ns == s;
}

int main()
{
    int t, kase = 0;
    cin >> t;
    while (t--)
    {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        string r1 = dfs(0, n, "R");
        string r2 = dfs(0, n, "P");
        string r3 = dfs(0, n, "S");
        string ans = "IMPOSSIBLE";
        if (valid(r1, r, p, s) && (ans == "IMPOSSIBLE" || r1 < ans)) ans = r1;
        if (valid(r2, r, p, s) && (ans == "IMPOSSIBLE" || r1 < ans)) ans = r2;
        if (valid(r3, r, p, s) && (ans == "IMPOSSIBLE" || r1 < ans)) ans = r3;
        cout << "Case #" << ++kase << ": " << ans << endl;
    }
    return 0;
}