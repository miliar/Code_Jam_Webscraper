#include <bits/stdc++.h>

using namespace std;

int main(){ freopen("in.txt", "r", stdin);
                freopen("out.txt", "w", stdout);
    int i, t, T;
    cin >> t;
    for(T = 1; T <= t; T++){
        cout << "Case #" << T << ": ";
        set <int> a;
        a.clear();
        int n;
        cin >> n;
        if(n == 0){
            cout << "INSOMNIA" << endl;
            continue;
        }
        int x = n;
        int y, r;
        for(i = 0;;i++){
            x = (i+1)*n;
            y = x;
            while(y != 0){
                r = y % 10;
                a.insert(r);
                y /= 10;
            }
            if(a.size() == 10){
                cout << x << endl;
                break;
            }
        }
    }
    return 0;
}
