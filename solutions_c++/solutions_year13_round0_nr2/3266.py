#include <iostream>
#include <stdio.h>
using namespace std;

#define MAX 110

int n, m;
int mat[MAX][MAX], max_ver[MAX], max_hor[MAX];

void init() {
    for (int i=0; i<n; ++i) {
        max_hor[i] = -1;
        for (int j=0; j<m; ++j) {
            if (max_hor[i] == -1 || max_hor[i] < mat[i][j])
                max_hor[i] = mat[i][j];
        }
    }
    for (int j=0; j<m; ++j) {
        max_ver[j] = -1;
        for (int i=0; i<n; ++i) {
            if (max_ver[j] == -1 || max_ver[j] < mat[i][j])
                max_ver[j] = mat[i][j];
        }
    }
}

bool isOK() {
    for (int i=0; i<n; ++i) {
        for (int j=0; j<m; ++j) {
            int d = min(max_hor[i], max_ver[j]);
            if (mat[i][j] < d)
                return false;
        }
    }

    return true;
}

int main() {
    // freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cs=1; cs<=t; ++cs) {
        scanf("%d%d", &n, &m);
        for (int i=0; i<n; ++i)
            for (int j=0; j<m; ++j)
                scanf("%d", &mat[i][j]);

        // for (int i=0; i<n; ++i) {
        //     for (int j=0; j<m; ++j)
        //         cout << mat[i][j] << " ";
        //     cout << endl;
        // }

        init();

        printf("Case #%d: ", cs);
        if (isOK())
            printf("YES\n");
        else
            printf("NO\n");
        
    }
    return 0;
}
