#include <iostream>
#include <stdlib>
#include <stdio>

typedef unsigned long long Int;

using namespace std;

Int solve() {
    Int l;
    Int cnt = 0, gotup = 0;
    int n;
    scanf("%llu", &l);
    //cout << "    ";
    for (Int i=0; i<=l; i++) {
        scanf("%1d", &n);
        if (i > 0) {
            if (n>0 && gotup < i) {
                cnt += i - gotup;
//                cout << "    Help: " << (i - gotup) << endl;
                gotup += i - gotup;
            }
        }
        gotup += n;

//        cout << "    " << n << "\tGotup: " << gotup << endl;
    }
    scanf("%c", &n);
    return cnt;
}


int main()
{
    freopen("A-large.in", "r", stdin);
   	//freopen("a.out", "w", stdout);
    Int cases = 123;
    scanf("%llu", &cases);
    for (int c=0; c < cases; c++) {
         cout << "Case #" << (c + 1) << ": " << solve() << endl;
//         return 0;
    }

    return 0;
}

