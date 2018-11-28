#include <iostream>
using namespace std;

typedef long long int lli;

lli lpow(lli n, lli e)
{
    lli ret = 1;
    if (!e)
        return 1;
    while (e--)
        ret *= n;
    return ret;
}

int main()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        lli K, C, S, KpowC, KpowC1;
        cin >> K >> C >> S;
        KpowC = lpow(K, C);
        KpowC1 = lpow(K, C - 1);
        if (S == K) {
            cout << "Case #" << t + 1 << ": ";
            for (long long i = 1; i < KpowC + 1; i += KpowC1)
                cout << i << ' ';
            cout << endl;
        }
    }
    return 0;
}
