#include <bits/stdtr1c++.h>

#define MAX 10010
#define clr(ar) memset(ar, 0, sizeof(ar))
#define read() freopen("lol.txt", "r", stdin)
#define dbg(x) cout << #x << " = " << x << endl
#define write() freopen("output.txt", "w", stdout)
#define valid(i, j) ((i) >= 0 && (i) < n && (j) >= 0 && (j) < m)

using namespace std;

const char* dir_str = "^>v<";
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

vector <int> adj[MAX];
bool visited[MAX], loop[MAX];
char str[105][105], pos[256];
int n, m, r, len, no_len, no_flag, no[MAX], T[MAX], counter[MAX];

void topsort(int i){
    visited[i] = true;
    if (i != r) T[len++] = i;

    int j, x, len = adj[i].size();
    for (j = 0; j < len; j++){
        x = adj[i][j];
        if (!visited[x]) topsort(x);
    }
}

void dfs(int i){
    if (i == r) no_flag = 1;
    else no[no_len++] = i;
    visited[i] = true;

    int j, x, len = adj[i].size();
    for (j = 0; j < len; j++){
        x = adj[i][j];
        if (!visited[x]) dfs(x);
    }
}

int main(){
    read();
    write();
    int fuck = 0, t, i, j, k, l, c, d, x, y, p;
    for (j = 0; dir_str[j] != 0; j++) pos[dir_str[j]] = j;

    scanf("%d", &t);
    while (t--){
        scanf("%d %d", &n, &m);
        for (i = 0; i < n; i++) scanf("%s", str[i]);

        r = n * m;
        for (i = 0; i < MAX; i++) adj[i].clear();

        for (i = 0; i < n; i++){
            for (j = 0; j < m; j++){
                if (str[i][j] != '.'){
                    x = (i * m) + j;

                    d = pos[str[i][j]];
                    k = i + dx[d], l = j + dy[d];

                    for (; ;){
                        if (!valid(k, l)){
                            adj[x].push_back(r);
                            break;
                        }
                        else if (str[k][l] != '.'){
                            y = (k * m) + l;
                            adj[x].push_back(y);
                            break;
                        }
                        k += dx[d], l += dy[d];
                    }
                }
            }
        }

        len = 0;
        clr(visited);
        for (i = 0; i < r; i++){
            visited[r] = false;
            if (!visited[i] && adj[i].size()) topsort(i);
        }
        reverse(T, T + len);

        int res = 0, flag = 0;
        clr(visited), clr(loop);

        for (i = 0; i < len; i++){
            x = T[i];
            if (!visited[x]){
                visited[r] = false;
                no_len = 0, no_flag = 0;
                dfs(x);

                if (!no_flag){
                    for (j = 0; j < no_len; j++) loop[no[j]] = 1;
                }
                else if (no_len != 1){
                    res++;
                    for (j = 0; j < no_len; j++) loop[no[j]] = 1;
                }
            }
        }

        for (p = 0; p < r; p++){
            if (adj[p].size() && !loop[p]){
                i = p / m;
                j = p % m;
                char ch = str[i][j];

                int found = 0;
                for (c = 0; c < 4; c++){
                    str[i][j] = dir_str[c];

                    d = pos[str[i][j]];
                    k = i + dx[d], l = j + dy[d];

                    for (; ;){
                        if (!valid(k, l)){
                            break;
                        }
                        else if (str[k][l] != '.'){
                            y = (k * m) + l;
                            if (loop[y]) found = 1;
                            else{
                                found = 1;
                                res++;
                                loop[y] = 1;
                            }
                            break;
                        }
                        k += dx[d], l += dy[d];
                    }
                    if (found) break;


                }
                str[i][j] = ch;

                if (!found){
                    flag = 1;
                    break;
                }

                res++;
                loop[p] = 1;
            }
        }

        if (flag) printf("Case #%d: IMPOSSIBLE\n", ++fuck);
        else printf("Case #%d: %d\n", ++fuck, res);
    }
    return 0;
}

/***

13

2 1
^
^

2 2
>v
^<

3 3
...
.^.
...

1 1
.

6 6
......
>>>v..
^..<..
^....v
^....v
.....v

6 6
......
>>>v..
^..<..
^....v
^.....
...^<v

6 6
......
>>>v..
...<..
^....v
^....v
.....v

6 6
......
>>>v..
...<..
^.^..v
^....v
..v..v

6 6
..v...
......
......
..v...
..v...
..>>.>

4 4
....
.^..
..v.
.>>.

4 4
>..<
.vvv
..^v
.^.v

4 4
.^.^
...v
...v
.v.v

3 3
^..
...
v..


Case #1: 1
Case #2: 0
Case #3: IMPOSSIBLE
Case #4: 0
Case #5: 1
Case #6: 1
Case #7: 2
Case #8: 3
Case #9: 1
Case #10: 2
Case #11: 1
Case #12: 4
Case #13: 2



***/
