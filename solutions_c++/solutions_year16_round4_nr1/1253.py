#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iostream>
using namespace std;

int n, r, s, p;
const int maxn = 12;
const string imp = "IMPOSSIBLE";
string ans[maxn + 2][3];
int pp[maxn + 2][3];
int rr[maxn + 2][3];
int ss[maxn + 2][3];


void work()
{
    ans[0][0] = "R";
    ans[0][1] = "S";
    ans[0][2] = "P";
    for (int i = 1; i <= maxn; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
            ans[i][j] = "";
            for (int l = 0; l < ans[i - 1][j].length(); ++l)
            {
                if (ans[i - 1][j][l] == 'R') ans[i][j] += "RS";
                if (ans[i - 1][j][l] == 'S') ans[i][j] += "PS";
                if (ans[i - 1][j][l] == 'P') ans[i][j] += "PR";
            }
            
            int cmp = 1;
            for (int l = 1; l < i; ++l)
            {
                cmp = 2 * cmp;
                int k = 0;
                while (k < ans[i][j].length())
                {
                    //cout << "* " << k << " " << ans[i][j].length() << " " << cmp << " " << ans[i][j] << endl;
                    if (ans[i][j].substr(k, cmp) > ans[i][j].substr(k + cmp, cmp))
                    {
                        for (int x = k; x < k + cmp; ++x)
                        {
                            char tmp = ans[i][j][x];  ans[i][j][x] = ans[i][j][x + cmp];  ans[i][j][x + cmp] = tmp;   
                        }
                    }
                    k += 2 * cmp;
                } 
            }
            
        }
        //cout << i << endl;
        //cout << ans[i][0] << endl << ans[i][1] << endl << ans[i][2] << endl;
    }
    
    for (int i = 1; i <= maxn; ++i)
    {
        for (int j = 0; j < 3; ++j)
        {
                pp[i][j] = rr[i][j] = ss[i][j] = 0;
                for (int k = 0; k < ans[i][j].length(); ++k)
                {
                    if (ans[i][j][k] == 'P') pp[i][j] ++;
                    if (ans[i][j][k] == 'S') ss[i][j] ++;
                    if (ans[i][j][k] == 'R') rr[i][j] ++;
                }
        }
    }
}

void init()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
    {
        cin >> n >> r >> p >> s;
        cout << "Case #" << i + 1 << ": ";
        string _ans = imp;
        if (r == rr[n][0] && p == pp[n][0] && s == ss[n][0]) _ans = ans[n][0];
        if (r == rr[n][1] && p == pp[n][1] && s == ss[n][1] && (_ans == imp || ans[n][1] < _ans)) _ans = ans[n][1];
        if (r == rr[n][2] && p == pp[n][2] && s == ss[n][2] && (_ans == imp || ans[n][2] < _ans)) _ans = ans[n][2];
        cout << _ans << endl;
    }
}


int main()
{
    work();
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    init();
    return 0;
} 
