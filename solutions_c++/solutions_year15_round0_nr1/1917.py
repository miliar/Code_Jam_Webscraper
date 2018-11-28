#include <iostream>
#include <iomanip>
#include <fstream>
#include <cstring>
using namespace std;

int main(int argc, char *argv[])
{
    int i, j, k;

    int t, num, cur, res;
    char tch;

    if (argc < 2) {
        printf(" need file in,out ");
        return -1;
    }
    freopen(argv[1], "rt", stdin);
    freopen(argv[2], "wt", stdout);

    cin >> t;
    for (i = 0; i<t; i++) {
        cin >> num;
        res = 0;
        cur = 0;
        for (j = 0; j<=num; j++) {
            cin >> tch;
            if (j>cur) {
                res++;      //need man
                cur++;
            }
            cur += tch-'0';
        }

        cout << "Case #" << i+1 << ": " << res << endl;
    }
}

