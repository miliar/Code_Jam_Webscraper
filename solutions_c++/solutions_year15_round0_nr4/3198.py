#include<iostream>
#include<vector>
#include<algorithm>
#include<cassert>
using namespace std;

unsigned int max(const unsigned int a, const unsigned int b) {
    if (a>b) return a;
    else return b;
}

unsigned int min(const unsigned int a, const unsigned int b) {
    if (a<b) return a;
    else return b;
}

bool canGabrielWin(const unsigned int x, const unsigned int r, const unsigned int c) {
    if (x<=3 && max(r,c) >= x && min(r,c) >= (x-1)/2+1 && r*c%x == 0) return true;
    if (x>3 && max(r,c) >= x && min(r,c) >= (x-1)/2+2 && r*c%x == 0) return true;
    return false;
}

int main() {
    unsigned int T;
    cin >> T;
    for (unsigned int t=0;t<T;++t) {
        unsigned int x,r,c;
        cin >> x >> r >> c;
        cout << "Case #" << (t+1) << ": " << (canGabrielWin(x,r,c)?"GABRIEL":"RICHARD") << std::endl;
    }
    return 0;
}
