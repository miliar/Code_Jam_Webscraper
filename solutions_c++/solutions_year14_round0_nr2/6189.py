#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 16 + 1;
int n, m;
int a[4][4] = {0};
int b[4][4] = {0};

int c[MAXN];

int T,TT;


int main()
{
    freopen("RQ_2_in.txt", "r", stdin);
    freopen("RQ_2_out.txt", "w", stdout);

    cin >> T;
    TT = 1;

    while(T) {
        double C,F,X;
        cin >> C >> F >> X;
        double time = 0.0;
        for (int i = 0 ;; i ++) {
            double x = (X)/(F * i + 2);
            double y = (C)/(F * i + 2) + (X)/ (F * (i + 1) + 2);
            if (y > x)
            {
                time += x;
                break;
            }
            time += (C)/(i * F + 2);
        }

        cout << "Case #" << TT << ": " << setprecision(6) << fixed << time << endl;
        T --;
        TT ++;
    }

    return 0;
}
/*
3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
*/

