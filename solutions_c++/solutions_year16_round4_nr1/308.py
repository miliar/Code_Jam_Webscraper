#include <bits/stdtr1c++.h>

#define MAX 200010
#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define dbg(x) cout << #x << " = " << x << endl
#define write() freopen("out.txt", "w", stdout)

using namespace std;

char str[MAX], out[MAX], cur[MAX], temp[MAX];
int n, r, p, s, m, h, nodes, nodes_str[MAX], nodes_temp[MAX];

string F(int i){
    int j, x;
    string res = string(1, cur[i]);
    if ((i * 2) <= h){
        string x = F(2 * i);
        string y = F(2 * i + 1);
        if (y < x) swap(x, y);
        res = x + y;
    }

    return res;
}

bool solve(char ch){
    int i, j, k, x, r1 = 0, p1 = 0, s1 = 0;

    h = 1, str[0] = ch, str[1] = 0, cur[1] = ch;
    for (i = 0; i < n; i++){
        strcpy(temp, str);
        for (j = 0, k = 0; temp[j]; j++){
            if (temp[j] == 'R') str[k++] = 'S', str[k++] = 'R';
            if (temp[j] == 'S') str[k++] = 'P', str[k++] = 'S';
            if (temp[j] == 'P') str[k++] = 'P', str[k++] = 'R';
        }
        str[k] = 0;
        for (j = 0; j < k; j++) cur[++h] = str[j];
    }

    for (i = 0; i < k; i++){
        if (str[i] == 'R') r1++;
        if (str[i] == 'P') p1++;
        if (str[i] == 'S') s1++;
    }
    if (r1 != r || p1 != p || s1 != s) return false;

    string s = F(1);
    strcpy(str, s.c_str());
    return true;
}

int main(){
    read();
    write();
    int T = 0, t, i, j, k;

    scanf("%d", &t);
    while (t--){
        scanf("%d %d %d %d", &n, &r, &p, &s);
        m = 1 << n;
        strcpy(out, "-1");

        if (solve('P') && (strcmp(out, "-1") == 0 || strcmp(str, out) < 0)) strcpy(out, str);
        if (solve('R') && (strcmp(out, "-1") == 0 || strcmp(str, out) < 0)) strcpy(out, str);
        if (solve('S') && (strcmp(out, "-1") == 0 || strcmp(str, out) < 0)) strcpy(out, str);

        if (strcmp(out, "-1") == 0) printf("Case #%d: IMPOSSIBLE\n", ++T);
        else printf("Case #%d: %s\n", ++T, out);
        fprintf(stderr, "%d", T);
    }
    return 0;
}
