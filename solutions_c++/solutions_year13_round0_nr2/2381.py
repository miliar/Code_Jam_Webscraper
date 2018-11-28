#include<iostream>
#include<cstdio>

using namespace std;

int a[200][200];
int max1[200], max2[200];

int main() {
    int ntest, m, n;
    bool ok;
    
    freopen("b.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    scanf("%d", &ntest);
    for(int test=0; test<ntest; test++) {
        cout << "Case #" << test+1 << ": ";
        scanf("%d%d", &m, &n);
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++)
                scanf("%d", &a[i][j]);
                
        for(int i=0; i<m; i++)
            max1[i] = 0;
        for(int i=0; i<n; i++)
            max2[i] = 0;
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++) {
                if (a[i][j] > max1[i]) max1[i] = a[i][j];
                if (a[i][j] > max2[j]) max2[j] = a[i][j];
            }
        
        bool ok = true;
        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++)
                if (max1[i] != a[i][j] && max2[j] != a[i][j]) {
                    ok = false;
                    break;
                }
            if (!ok) break;
        }
        if (!ok) cout << "NO";
         else cout << "YES";
        cout << endl;
    }
    
    return 0;
}
