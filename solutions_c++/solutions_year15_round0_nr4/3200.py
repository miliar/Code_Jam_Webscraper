
#include <iostream>
using namespace std;

void sol(int i, bool ok){
    cout << "Case #" << i+1 << ": " << (ok ? "GABRIEL" : "RICHARD") << endl;
}

int main() {
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        int x,r,c; cin >> x >> r >> c;
        if (x == 1) sol(i,true);
        if (x == 2){
            if ((r * c) % 2 != 0) sol(i, false);
            else sol(i, true);
        }
        if (x == 3){
            if ((r * c) % 3 != 0) sol(i, false);
            else if (r < 2 || c < 2) sol(i, false);
            else sol(i, true);
        }
        if (x == 4){
            if (r * c == 12 || r * c == 16) sol(i, true);
            else sol(i, false);
        }
        
    }
    return 0;
}
