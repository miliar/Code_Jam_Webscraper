#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <iomanip>
#include <map>
#include <queue>
#define pb push_back
#define mp make_pair
#define pp pair<int,int>
#define ppp pair<pp, pp>
#define pl pair<ll, ll>
#define p3 pair<pl, pp>
#define fi first
#define se second
typedef long long ll;
typedef long double ld;
using namespace std;
int nTest;
int R, C;
string s[110];


int main()
{
    ios::sync_with_stdio(false);
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin>>nTest;
    for (int kk = 1; kk <= nTest; kk++)
    {
        cin>>R>>C;
        for (int i = 0; i < R; i++)
             cin>>s[i];
        bool ok = true;
        int res = 0;
        for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
        if (s[i][j] != '.')
        {
            bool u = false, d = false, l = false, r = false;
            for (int k = i - 1; k >= 0; k--)
                 if (s[k][j] != '.') u = true;
            for (int k = i + 1; k < R; k++)
                if (s[k][j] != '.') d = true;

            for (int k = j - 1; k >= 0; k--)
                if (s[i][k] != '.') l = true;
            for (int k = j + 1; k < C; k++)
                if (s[i][k] != '.') r = true;

            if (u == false && d == false && l == false && r == false)
                ok = false;
                else
                {
                    bool is = false;
                    if (s[i][j] == '>' && r ) is = true;
                    if (s[i][j] == '<' && l ) is = true;
                    if (s[i][j] == 'v' && d ) is = true;
                    if (s[i][j] == '^' && u ) is = true;
                    if (is == false) res++;
                }
        }
        if (ok == false)
        cout<<"Case #"<<kk<<": "<<"IMPOSSIBLE"<<"\n";
            else
            cout<<"Case #"<<kk<<": "<<res<<"\n";
    }

    return 0;
}
