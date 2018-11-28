#include <iostream>
#include <cstdio>
#define SZ(X) ((int)((X).size()))
using namespace std;

int t, vst, l, a[105], b[105];
bool c[105];
string s;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
    freopen ("A-large.in", "r", stdin);
    freopen ("A-large.out", "w", stdout);
    cin >> t;
    for (int q = 0; q < t; q++){
        cin >> s; vst = 0, l = SZ(s);
        for (int i = 0; i < 100; i++){
            a[i] = 0; b[i] = 0; c[i] = false;
        }
        for (int i = 0; i < l; i++)
            a[i] = s[l-i-1]-'0';
        for (int i = 0; i < 100 && vst < 10; i++){
            for (int j = 0; j < 100; j++)
                b[j] += a[j];
            for (int j = 0; j < 100; j++)
                while (b[j] > 9){
                    b[j+1]++;
                    b[j] -= 10;
                }
            while (b[l] > 0) l++;
            for (int j = 0; j < l; j++)
                if (c[b[j]] == false){
                    vst++; c[b[j]] = true;
                }
        }
        cout << "Case #" << q+1 << ": ";
        if (vst < 10)
            cout << "INSOMNIA";
        else
            for (int i = l-1; i >= 0; i--)
                cout << b[i];
        cout << "\n";
    }
    return 0;
}
