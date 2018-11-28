#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 100 + 1;
int n, m;

int a[MAXN][MAXN] = {0};
char c[MAXN] = {0};
char ct[MAXN] = {0};

int T,TT;

int main()
{
    freopen("R1B_1_in.txt", "r", stdin);
    freopen("R1B_1_out.txt", "w", stdout);

    cin >> T;
    TT = 1;

    while(T) {
        memset(a,0,sizeof(a));
        memset(ct,0,sizeof(ct));

        cin >> n;
        string s;
        cin >> s;

        int charn = 0;
        char pat = ' ';
        for (int j = 0; j < s.length(); j ++) {
            if (s[j] != pat) {
                a[charn][0] ++;
                ct[charn] = s[j];
                pat = s[j];
                charn ++;
            }
            else
                a[charn - 1][0] ++;
        }

        m = charn;

        bool fail = 0;
        for (int i = 1; i < n; i ++) {
            memset(c,0,sizeof(c));
            cin >> s;
            int charn = 0;
            char pat = ' ';
            for (int j = 0; j < s.length(); j ++) {
                if (s[j] != pat) {
                    a[charn][i] ++;
                    c[charn] = s[j];
                    pat = s[j];
                    charn ++;
                }
                else
                    a[charn - 1][i] ++;
            }

            if (charn != m) {
                fail = 1;
                break;
            }

            for (int j = 0; j < m; j ++)
                if(ct[j] != c[j])
                {
                    fail = 1;
                    break;
                }
            if (fail)
                break;

            /*
            charn = 0;
            for (int j = 0; j < s.length(); j ++) {
                if (s[j] != c[charn]) {
                    if (a[charn][i] == 0) {
                        fail = 1;
                        break;
                    }
                    charn ++;
                    if (charn == m || s[j] != c[charn]) {
                        //cout << charn << " " << m << " " << s[j] << " " << c[charn] << endl;
                        fail = 1;
                        break;
                    }
                    else
                        a[charn][i] ++;
                }
                else
                    a[charn][i] ++;
            }

            if (fail)
                break;*/
        }
        cout << "Case #" << TT << ": ";
        if(fail)
            cout << "Fegla Won";
        else {

            /*for (int i = 0; i < n; i ++)
            {
                for (int j = 0; j < m; j ++)
                {
                    cout << c[j]  << "|" << a[j][i] << ' ';
                }
                cout << endl;
            }*/

            int ss = 0;
            for (int j = 0; j < m; j ++)
            {
                sort(&a[j][0], &a[j][n]);
                int s = 0;
                for (int i = 0; i < n; i ++)
                {
                    if (a[j][i] - a[j][n/2] > 0)
                        s += a[j][i] - a[j][n/2];
                    else
                        s += a[j][n/2] - a[j][i];
                }
                ss += s;
                //cout << s << ' ';
            }
            cout << ss ;
        }
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

