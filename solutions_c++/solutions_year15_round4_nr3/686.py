#include <bits/stdtr1c++.h>

#define MAX 21
#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define dbg(x) cout << #x << " = " << x << endl
#define write() freopen("output.txt", "w", stdout)

using namespace std;

char in[100010], str[MAX][100010];
int t, n, res, len[MAX], adj[MAX][1010];
const unsigned int base = 1925728309U;

inline void backtrack(int i, int counter, tr1::unordered_map <unsigned int, char>& mp){
    if (counter >= res) return;

    if (i == n){
        res = min(res, counter);
        return;
    }

    int j, x, p, y;

    if (i != 1){
        y = 0;
        tr1::unordered_map <unsigned int, char> temp = mp;

        for (j = 0; j < len[i]; j++){
            unsigned int h = adj[i][j];
            x = temp[h];
            p = x;
            x |= 1;
            if (x == 3 && p != 3) y++;
            temp[h] = x;
        }
        backtrack(i + 1, counter + y, temp);
    }

    if (i != 0){
        y = 0;
        tr1::unordered_map <unsigned int, char> temp = mp;

        for (j = 0; j < len[i]; j++){
            unsigned int h = adj[i][j];
            x = temp[h];
            p = x;
            x |= 2;
            if (x == 3 && p != 3) y++;
            temp[h] = x;
        }
        backtrack(i + 1, counter + y, temp);
    }
}

int main(){
    read();
    write();
    int T = 0, i, j, k, l, x, y;

    gets(in);
    t = atoi(in);
    while (t--){
        gets(in);
        n = atoi(in);
        for (i = 0; i < n; i++) gets(str[i]);

        clr(len);
        for (i = 0; i < n; i++){
            strcpy(in, str[i]);
            char* pch = strtok(in, " ");
            while (pch != 0){
                unsigned int x = 0;
                for (j = 0; pch[j]; j++) x = (x * base) + pch[j];
                adj[i][len[i]++] = x;
                pch = strtok(0, " ");
            }
        }

        res = 1 << 20;
        tr1::unordered_map <unsigned int, char> mp;
        backtrack(0, 0, mp);

        printf("Case #%d: %d\n", ++T, res);
    }
    return 0;
}
