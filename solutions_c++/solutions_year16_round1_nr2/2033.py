# include <bits/stdc++.h>

using namespace std;

int main() {

    int vet[3000];
    int t, n, x, I = 0;
    cin >> t;

    while(t--) {
        memset(vet, 0, sizeof vet);
        cin >> n;
        for (int i = 0; i < (2*n-1)*n; ++i) {
            cin >> x;
            ++vet[x];
        }

        cout << "Case #" << ++I << ":";
        for (int i = 0; i < 2510; ++i) {
            if(vet[i] && vet[i]%2 == 1) {
                cout << " " << i;
            }
        }
        cout << endl;

    }
    return 0;
}
