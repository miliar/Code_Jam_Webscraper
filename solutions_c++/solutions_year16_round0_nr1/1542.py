
#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for (int i = 0; i < int(n); i++)
#define rep1(i,n) for (int i = 1; i <= int(n); i++)
#define var(x) #x " = " << x
#define show(x) cout << var(x) << endl;
#define all(c) (c).begin(), (c).end()
#define fst first
#define snd second
#define pb push_back

int main() {
    int T;
    cin >> T;
    rep1 (t,T) {
        cout << "Case #" << t << ": ";
        int N;
        cin >> N;
        if (N == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        bool digit[10];
        rep (i,10) digit[i] = false;
        
        int NN = N;
        while (true) {
            int M = NN;
            while (M > 0) {
                digit[M % 10] = true;
                M /= 10;
            }
            
            bool flag = false;
            rep (i,10) if (!digit[i]) flag = true;
            if (!flag) {
                cout << NN << endl;
                break;
            }
            NN += N;
        }
    }
}
