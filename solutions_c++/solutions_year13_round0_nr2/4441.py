#include <iostream>
#include <cstdio>

using namespace std;

#define MAX_SIZE 100
int colMax[MAX_SIZE];
int rowMax[MAX_SIZE];
int lawn[MAX_SIZE][MAX_SIZE];


bool solve() {
    int i,j,n,m;
    scanf("%d %d", &n, &m);
    for (i = 0; i < n; i++) {
        for (j = 0 ; j < m; j++) {
            scanf("%d", &lawn[i][j]);
        }
    }

    for (i = 0; i < n; i++) {
        rowMax[i] = lawn[i][0];
        for (j = 0 ; j < m; j++) {
            if (lawn[i][j] > rowMax[i])
                rowMax[i] = lawn[i][j];
        }
    }

    for (i = 0; i < m; i++) {
        colMax[i] = lawn[0][i];
        for (j = 0 ; j < n; j++) {
            if (lawn[j][i] > colMax[i])
                colMax[i] = lawn[j][i];
        }
    }

    for (i = 0; i < n; i++) {
        for (j = 0 ; j < m; j++) {
            if (lawn[i][j] < rowMax[i] && lawn[i][j] < colMax[j])
                return false;
        }
    }
    return true;
}

char yes[] = "YES";
char no[] = "NO";

char* getStatus(bool res) {
    if (res)
        return yes;
    return no;
}

int main()
{
    int t;
    scanf("%d\n", &t);
    bool res;
    for (int i = 1; i <= t; i++) {
        res = solve();
        printf("Case #%d: %s\n", i, getStatus(res));
    }
    return 0;
}
