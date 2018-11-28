#include <iostream>

using namespace std;
typedef unsigned int uint;

void run(uint nTst);
void output(uint nTst, bool ans);

int main()
{
    uint T;
    cin >> T;
    for(uint i = 0; i < T; ++i)
        run(i + 1);
    return 0;
}

void run(uint nTst) {
    uint X, R, C;
    cin >> X >> R >> C;
    if(R > C) {
        uint tmp = R;
        R = C;
        C = tmp;
    }

    bool ans = ((R * C) % X == 0);
    if(ans) {
        if(X == 3) {
            ans = (R > 1);
        }
        if(X == 4) {
            if(C == 4 && R >= 3) ans = true;
            else ans = false;
        }
    }
    output(nTst, ans);
}

void output(uint nTst, bool ans) {
    cout << "Case #" << nTst << ": ";
    if(ans) cout << "GABRIEL";
    else cout << "RICHARD";
    cout << endl;
}
