#include <iostream>

using namespace std;

int main(){
    int t, i, x, r, c, res;
    
    cin >> t;
    for (i = 0; i < t; i++){
        cin >> x >> r >> c;
        res = 0;
        if (x == 1)
            res = 1;
        if (x == 2 && (r * c) % 2 == 0)
            res = 1;
        if (x == 3 && ((r * c) % 6 == 0 || (r * c) % 9 == 0))
            res = 1;
        if (x == 4 && ((r * c) % 12 == 0 || (r * c) % 16 == 0))
            res = 1;
            
        cout << "Case #" << i+1 << ": ";
        if (res == 0) cout << "RICHARD";
        else cout << "GABRIEL";
        if (i+1 < t) cout << endl;
    }
    
    return 0;
}
