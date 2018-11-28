#include <iostream>
#include <algorithm>
using namespace std;

void solve(int testcase);

int main() {
    int N;
    cin >> N;
    for(int i=0; i<N; ++i)
        solve(i+1);
}

void solve(int testcase) {
    unsigned X,R,C;
    cin >> X >> R >> C;
    if((X <= R || X <= C) && ((X+1)/2) <= min(R,C) && (R*C)%X == 0 && X < 7) {
        if(!(X==R*C/2 && X>=4)) {
            cout << "Case #" << testcase << ": GABRIEL" << endl;
            return;
        }
    }
    cout << "Case #" << testcase << ": RICHARD" << endl;
}
