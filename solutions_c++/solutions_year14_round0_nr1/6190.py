#include <iostream>
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
    freopen("RQ_1_in.txt", "r", stdin);
    freopen("RQ_1_out.txt", "w", stdout);

    cin >> T;
    TT = 1;

    while(T) {
        cin >> n;
        for (int i = 0; i < 16; i ++)
            cin >> a[i/4][i%4];
        cin >> m;
        for (int i = 0; i < 16; i ++)
            cin >> b[i/4][i%4];

        memset(c,0,sizeof(c));
        for (int i = 0; i < 4; i ++)
            c[a[n - 1][i]] += 1;
        for (int i = 0; i < 4; i ++)
            c[b[m - 1][i]] += 1;

        int d = 0, k = 0;
        for (int i = 0; i <= 16; i ++) {
            if (c[i] == 2) {
                k ++;
                d = i;
            }
            //cout << c[i] << " ";
        }

        cout << "Case #" << TT << ": ";

        if (k == 0)
            cout << "Volunteer cheated!";
        else if (k >= 2)
            cout << "Bad magician!";
        else
            cout << d;
        cout << endl;
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

