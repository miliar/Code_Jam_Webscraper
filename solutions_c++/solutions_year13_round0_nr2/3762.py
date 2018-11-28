#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;
const char* fi = "B-large.in";
const char* fo = "output.txt";
const int maxn = 110;

int a[maxn][maxn];
int maxR[maxn], maxC[maxn];
int n,m;

void ReadFile();
bool Ok(int x, int y);
bool Check();

int main()
{
    freopen(fi,"r",stdin);
    freopen(fo,"w",stdout);
    int nTest;
    cin >> nTest;
    for (int test=1; test<=nTest; test++)
    {
        ReadFile();
        cout << "Case #" << test << ": ";
        if (Check()) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}

void ReadFile()
{
    cin >> n >> m;
    for (int i=1; i<=n; i++) maxR[i] = 0;
    for (int j=1; j<=m; j++) maxC[j] = 0;
    for (int i=1; i<=n; i++)
        for (int j=1; j<=m; j++)
        {
            cin >> a[i][j];
            if (a[i][j]>maxR[i]) maxR[i] = a[i][j];
            if (a[i][j]>maxC[j]) maxC[j] = a[i][j];
        }
}

bool Ok(int x, int y)
{
    /*int xx = 0, yy = 0;
    for (int i=1; i<=n; i++)
        if (a[i][y]>yy) yy = a[i][y];
    for (int j=1; j<=m; j++)
        if (a[x][j]>xx) xx = a[x][j];
    */
    if (maxR[x]>a[x][y] && maxC[y]>a[x][y]) return(false);
    return true;
}

bool Check()
{
    for (int i=1; i<=n; i++)
        for (int j=1; j<=m; j++)
            if (!Ok(i,j)) return(false);
    return true;
}
