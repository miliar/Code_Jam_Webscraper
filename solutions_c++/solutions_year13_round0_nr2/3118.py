#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void solve(int caseNum)
{
    // SOLVE TASK HERE!

    // read input
    int n, m;
    scanf("%d%d", &n, &m);

    vector< vector<int> > a(n, vector<int>(m));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            scanf("%d", &a[i][j]);
        }
    }

    // get maximum value of each row and column
    vector<int> rowMax(n, 0);
    vector<int> colMax(m, 0);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            rowMax[i] = max(rowMax[i], a[i][j]);
            colMax[j] = max(colMax[j], a[i][j]);
        }
    }

    // check 
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] < rowMax[i] && a[i][j] < colMax[j]) {
                printf("Case #%d: NO\n", caseNum);
                return;
            }
        }
    }

    printf("Case #%d: YES\n", caseNum);
}


int main()
{
    int T;
    scanf("%d\n", &T);

    for (int caseNum = 1; caseNum <= T; ++caseNum) {
        solve(caseNum);
    }

    return 0;
}

