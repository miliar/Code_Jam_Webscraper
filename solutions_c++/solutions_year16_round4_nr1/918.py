#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MXN = 13;
char c[]="RPS";

string seq[MXN][3];
int cn[MXN][3][3];

static void init()
{
    for (int i=0; i<3; i++)
    {
        seq[0][i] = std::string(1, c[i]);
        cn[0][i][i] = 1;
    }
    for (int i=1; i<MXN; i++)
    {
        for (int j=0; j<3; j++)
        {
            int b = (j+2)%3;
            for (int k=0; k<3; k++) cn[i][j][k] = cn[i-1][j][k] + cn[i-1][b][k];
            if (seq[i-1][j] < seq[i-1][b])
                seq[i][j] = seq[i-1][j] + seq[i-1][b];
            else
                seq[i][j] = seq[i-1][b] + seq[i-1][j];
   //         cout << "n " << i << " " << j << " " << c[j] << " " << cn[i][j][0] << " "
   //             << cn[i][j][1] << " " << cn[i][j][2] << " " << seq[i][j] << "\n";
        }
    }
}

std::string solve(int n, int r, int p, int s)
{
    vector<string> ans;
    for (int i=0; i<3; i++)
    {
        if (cn[n][i][0] == r && cn[n][i][1] == p && cn[n][i][2] == s)
        {
            ans.push_back(seq[n][i]);
        }
    }

    if (ans.empty()) return "IMPOSSIBLE";
    sort(ans.begin(), ans.end());
    return ans[0];
}

int main()
{
    init();
    int t;
    cin >>t;
    for (int i=1; i<=t; i++)
    {
        int n, r, p, s;
        cin >> n >> r >> p >> s;
        cout << "Case #" << i << ": " << solve(n, r, p, s) << "\n";
    }
}
