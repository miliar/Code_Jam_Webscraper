#include <bits/stdc++.h>

#define ll long long

using namespace std;

char buf[100];
char bufcpy[100];

int main()
{
    #ifdef FILEIO
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);

    int T;
    //scanf("%d\n", &T);
    cin >> T;
    for (int test = 1; test <= T; test++) {
        int k;
        string str;
        cin >> str >> k;

        int n = str.length();
        int flip_cnt = 0;
        int idx = 0;
        while (str[idx] == '+' && idx < n)
            idx++;

        bool possible = true;
        while (idx < n && possible) {
            if (idx + k > n)
                possible = false;
            else {
                flip_cnt++;
                for (int i = 0; i < k; i++) {
                    char &ch = str[idx+i];
                    if (ch == '+')
                        ch = '-';
                    else
                        ch = '+';
                }

                while (str[idx] == '+' && idx < n)
                    idx++;
            }
        }

        cout << "Case #" << test << ": ";
        if (possible)
            cout << flip_cnt << endl;
        else 
            cout << "IMPOSSIBLE" << endl;
    }
    
}
