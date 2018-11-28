#include <bits/stdc++.h>

#define ull unsigned long long

using namespace std;

const int MAXN = 1e6 + 5;

void task(int n, int t){
    vector <bool> dig(10, false);
    cout << "Case #" << t << ": ";
    if (!n){
        cout << "INSOMNIA" << endl;
        return;
    }
    int counter = 0;
    ull step = n;
    while (true){
        counter++;
        ull mem = n;
        while (n){
            dig[n % 10] = true;
            n /= 10;
        }
        bool done = true;
        for (int i = 0; i < 10; i++){
            if (!dig[i]){
                done = false;
                break;
            }
        }
        if (done){
            cout << mem << endl;
            return;
        }
        if (counter > (int)1e6){
            cout << "INSOMNIA" << endl;
        }
        n = mem + step;
    }
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, n;
    cin >> T;
    for (int t = 0; t < T; t++){
        cin >> n;
        task(n, t + 1);
    }
    return 0;
}
