#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <sstream>
#include <ctime>
#include <set>
#define  N   362
#define  M   1200
#define  inf 0XFFFFFFFFFFFFFFll
#define  mod 1000000007
#define  LL  long long
#define  eps 1e-12
#define  pi  acos(-1.0)

using namespace std;


ifstream fi("B-large.in");
#define cin fi
ofstream fo("B-large.out");
#define cout fo


int a[N][N], last[N][N];

int main()
{
    int cases; cin >> cases;
    for (int c=1; c<=cases; c++) {
        cout << "Case #" << c << ": ";
        int n, m; cin >> n >> m;
        for (int i=1; i<=n; i++)
            for (int j=1; j<=m; j++)
                cin >> a[i][j];
        for (int i=1; i<=n; i++) {
            int h = a[i][1];
            for (int j=1; j<=m; j++)
                h = max(h, a[i][j]);
            for (int j=1; j<=m; j++)
                last[i][j] = h;
        }
        for (int i=1; i<=m; i++) {
            int h = a[1][i];
            for (int j=1; j<=n; j++)
                h = max(h, a[j][i]);
            for (int j=1; j<=n; j++)
                last[j][i] = min(last[j][i], h);
        }
        bool flag = true;
        for (int i=1; i<=n; i++)
            for (int j=1; j<=m; j++)
                if (last[i][j] != a[i][j])
                    flag = false;
        if (flag)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}

