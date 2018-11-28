#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    int *temp = new int[1000000];
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int result = 1;

        int X, R, C;
        cin >> X >> R >> C;
        if (R*C < X || R*C%X != 0)
            result = 0;
        if (max(R,C) < X || min(R,C) < (X+1)/2 || min(R,C) < X-1)
            result = 0;

        cout << "Case #" << t+1 << ": " << (result==0?"RICHARD":"GABRIEL") << endl;
    }
    delete[] temp;
    return 0;
}
