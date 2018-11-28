#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int main()
{
    freopen("bin.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cases; cin >> cases;
    for (int i=1; i<=cases; i++)
    {
        int n, m; cin >> n >> m;
        int lawn[n][m];
        for (int j=0; j<n; j++) for (int k=0; k<m; k++) cin >> lawn[j][k];
        bool cut[n][m]; memset(cut, false, sizeof cut);
        for (int j=0; j<n; j++)
        {
            int maxa = -1; for (int k=0; k<m; k++) maxa = max(lawn[j][k], maxa);
            for (int k=0; k<m; k++) if (lawn[j][k] == maxa) cut[j][k] = true;
        }
        for (int j=0; j<m; j++)
        {
            int maxa = -1; for (int k=0; k<n; k++) maxa = max(lawn[k][j], maxa);
            for (int k=0; k<n; k++) if (lawn[k][j] == maxa) cut[k][j] = true;
        }
        bool cutter = true;
        for (int j=0; j<n; j++) for (int k=0; k<m; k++) cutter = (cutter && cut[j][k]);
        cout << "Case #" << i << ": " << (cutter?"YES":"NO") << endl;
    }
    return 0;
}
