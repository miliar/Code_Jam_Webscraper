#include <iostream>

using namespace std;
typedef unsigned int uint;

void run(uint nTst);
void output(uint nTst, uint ans);

int main()
{
    uint T;
    cin >> T;
    for(uint i = 0; i < T; ++i)
        run(i+1);
    return 0;
}

void run(uint nTst) {
    uint Smax;
    cin >> Smax;
    uint *Shy = new uint [Smax + 1];
    for(uint i = 0; i <= Smax; ++i) {
        char nShy;
        cin >> nShy;
        Shy[i] = nShy - '0';
    }

    uint ans = 0;
    uint alreadyClap = Shy[0];
    for(uint k = 1; k <= Smax; ++k) {
        uint needMore = 0;
        if(alreadyClap < k) needMore = k - alreadyClap;
        alreadyClap += Shy[k] + needMore;
        ans += needMore;
    }
    output(nTst, ans);
}

void output(uint nTst, uint ans) {
    cout << "Case #" << nTst << ": " << ans << endl;
}
