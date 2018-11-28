#include <iostream>

using namespace std;

const string G = "GABRIEL";
const string R = "RICHARD";

string solve(int x, int r, int c) {
    if(x == 1) {
        return G;
    }
    if(x == 2) {
        if((r * c) % 2 != 0) {
            return R;
        } else {
            return G;
        } 
    }
    if(x == 3) {
        if((r * c) % 3 != 0) {
            return R;
        }
        if(r < 2 || c < 2) {
            return R;
        }
        return G;
    }
    if(x == 4) {
        if((r * c) % 4 != 0) {
            return R;
        }
        if(r < 3 || c < 3) {
            return R;
        }
        return G;
    }
    return "";
}

int main() {
    int n;
    cin >> n;

    for(int i = 0; i < n; ++i) {
        int x,r,c;
        cin >> x >> r >> c;

        cout << "Case #" << (i+1) << ": " << solve(x,r,c) << endl;
    }

    return 0;
}
