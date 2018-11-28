#include <iostream>
#include <vector>
using namespace std;

void print(vector< vector< char > > &a, int r, int c){
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++)
            putchar(a[i][j]);
        putchar('\n');
    }
}

void solve() {
    int r, c, m;
    cin >> r >> c >> m;
    int n = r * c - m;
    
    if (n == 1) {
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++)
                if (!i && !j)
                    putchar('c');
                else
                    putchar('*');
            putchar('\n');
        }
        return;
    }

    if (r == 1 || c == 1) {
        putchar('c');
        if (c == 1) putchar('\n');
        for (int i = 1; i < n; i++) {
            putchar('.');
            if (c == 1) putchar('\n');
        }
        for (int i = 0; i < m; i++) {
            putchar('*');
            if (c == 1) putchar('\n');
        }
        if (r == 1 && c != 1) putchar('\n');
        return;
    }

    vector< vector< char > > a(r, vector<char>(c, '*'));
    for (int i = 2; i <= r; i++)
        for (int j = 2; j <= c; j++)
            if (i * j >= n) {
                if (i == 2 || j == 2) {
                    if (i * j == n) {
                        for (int u = 0; u < i; u++)
                            for (int v = 0; v < j; v++)
                                a[u][v] = '.';
                        a[0][0] = 'c';
                        //cout << 1 << endl;
                        print(a, r, c);
                        return;
                    } else 
                        continue;
                }
                if ((i == 3) && (i - 1) * j + 2 <= n) {
                    for (int u = 0; u < i - 1; u++)
                        for (int v = 0; v < j; v++)
                            a[u][v] = '.';
                    a[0][0] = 'c';
                    for (int v = 0; v < n - (i - 1) * j; v++)
                        a[i - 1][v] = '.';
                    //cout << 2 << endl;
                    print(a, r, c);
                    return;
                }
                if ((j == 3) && (j - 1) * i + 2 <= n) {
                    for (int v = 0; v < j - 1; v++)
                        for (int u = 0; u < i; u++)
                            a[u][v] = '.';
                    a[0][0] = 'c';
                    for (int u = 0; u < n - (j - 1) * i; u++)
                        a[u][j - 1] = '.';
                    //cout << 3 << endl;
                    print(a, r, c);
                    return;
                } 
                if (i >= 4 && (i - 2) * j + 4 <= n) {
                    for (int u = 0; u < i - 2; u++)
                        for (int v = 0; v < j; v++)
                            a[u][v] = '.';
                    for (int v = 0; v < min(n - (i - 2) * j - 2, j); v++)
                        a[i - 2][v] = '.';
                    for (int v = 0; v < n - (i - 2) * j - min(n - (i - 2) * j - 2, j); v++)
                        a[i - 1][v] = '.';
                    //cout << 4 << endl;
                    a[0][0] = 'c';
                    print(a, r, c);
                    return;
                }
                if (j >= 4 && (j - 2) * i + 4 <= n) {
                    for (int u = 0; u < i; u++)
                        for (int v = 0; v < j - 2; v++)
                            a[u][v] = '.';
                    for (int u = 0; u < min(n - (j - 2) * i - 2, i); u++)
                        a[u][j - 2] = '.';
                    for (int u = 0; u < n - (j - 2) * i - min(n - (j - 2) * i - 2, i); u++)
                        a[u][j - 1] = '.';
                    a[0][0] = 'c';
                    //cout << 5 << endl;
                        
                    print(a, r, c);
                    return;
                }
            }
    puts("Impossible");
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d:\n", i);
        solve();
    }   
}
