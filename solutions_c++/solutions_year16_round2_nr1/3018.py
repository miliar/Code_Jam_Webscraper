#include <iostream>
#include <cstdio>
#define SZ(X) ((int)((X).size()))
using namespace std;

int t, a[30], b[10][30], ans[20], m[20] = {0, 9, 1, 5, 6, 7, 2, 4, 3, 8};
string s;
string n[10] = {"ZERO", "TWO", "SIX", "EIGHT", "SEVEN", "THREE", "FOUR", "FIVE", "NINE", "ONE"};

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    freopen ("A-large.in", "r", stdin);
    freopen ("A-large.out", "w", stdout);
    cin >> t;
    for (int i = 0; i < 10; i++)
        for (int j = 0; j < SZ(n[i]); j++)
            b[i][n[i][j]-'A']++;
    for (int q = 0; q < t; q++){
        cin >> s;
        for (int i = 0; i < SZ(s); i++)
            a[s[i]-'A']++;
        for (int i = 0; i < 10; i++){
            int x = 1e5;
            for (int j = 0; j < 26; j++)
                if (b[i][j] > 0)
                    x = min(x, a[j]/b[i][j]);
            if (x == 1e5) x = 0;
            for (int j = 0; j < 26; j++)
                if (b[i][j] > 0)
                    a[j] = a[j]-(x*b[i][j]);
            ans[i] = x;
        }
        cout << "CASE #" << q+1 << ": ";
        for (int i = 0; i < 10; i++)
            for (int j = 0; j < ans[m[i]]; j++)
                cout << i;
        cout << "\n";
        for (int i = 0; i < 28; i++) a[i] = 0;
        for (int i = 0; i < 10; i++) ans[i] = 0;
    }
    return 0;
}
