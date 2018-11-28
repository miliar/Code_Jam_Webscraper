#include<bits/stdc++.h>

using namespace std;

long long maxx, t, n;
bool b[100];

main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large2.out", "w", stdout);
    cin >> t;
    for (int ii = 0; ii < t; ii++){
        cin >> n;
        if (n == 0)cout << "Case #" << ii + 1 << ": " << "INSOMNIA" << endl;
        else{
        for (int i = 0; i <= 9; i++) b[i] = false;
        long long t = 0;
        long long numb = 1;
        long long x = n;
        while (t < 10){
            long long x1 = x;
            while (x1 > 0){
                if (!b[x1 % 10]){
                    t++;
                    b[x1 % 10] = true;
                }
                x1 = x1 / 10;
            }
            numb++;
            x = numb * n;
        }
        cout << "Case #" << ii + 1 << ": " << (numb - 1) * n << endl;
        }
    }
}


