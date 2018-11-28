#include <fstream>
#include <cstring>
using namespace std;

int t, test, i, j, n, m, a[110][110], maxL[110], maxC[110];
bool ok;

int main()
{
    ifstream fi("test.in");
    ofstream fo("test.out");
    fi >> t;
    for(test = 1; test <= t; test++)
    {
        fi >> n >> m;
        memset(maxL, 0, sizeof(maxL));
        memset(maxC, 0, sizeof(maxC));
        ok = 1;
        for(i = 1; i <= n; i++)
            for(j = 1; j <= m; j++)
            {
                fi >> a[i][j];
                maxL[i] = max(maxL[i], a[i][j]);
                maxC[j] = max(maxC[j], a[i][j]);
            }
        for(i = 1; i <= n and ok; i++)
            for(j = 1; j <= m and ok; j++)
                if(maxC[j] > a[i][j] and maxL[i] > a[i][j]) ok = 0;
        fo << "Case #" << test << ": ";
        if(ok) fo << "YES\n"; else fo << "NO\n";
    }
    return 0;
}
