#include <cstdio>
#include <map>
#include <cstring>
#include <string>

using namespace std;

map<string, int> number;
map<int, bool> appear;

int known[3010];
int unknown[3010];

int base;

char sentence[1000000];
char word[30][1010][15];
int wn[30];
int w[30][1010];
int once[210];

int main() {
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        int n;
        scanf("%d\n", &n);
        int m = 0;
        number.clear();
        for (int i = 0; i < n; i++) {
            gets(sentence);
            int len = strlen(sentence);
            wn[i] = 0;
            int j = 0;
            while (j < len) {
                while (j < len && sentence[j] == ' ') j++;
                if (j == len) break;
                sscanf(sentence + j, "%s", word[i][wn[i]]);
                if (number[word[i][wn[i]]] == 0)
                    number[word[i][wn[i]]] = ++m;
                w[i][wn[i]] = number[word[i][wn[i]]];
                //printf("word : %s\n", word[i][wn[i]]);
                j += strlen(word[i][wn[i]]);
                wn[i]++;
            }
        }
        memset(known, 0, sizeof(known));
        memset(unknown, 0, sizeof(unknown));
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < wn[i]; j++)
                known[ w[i][j] ] |= 1 << i;
        base = 0;
        for (int i = 1; i <= m; i++)
            if (known[i] == 3) base++;
        int ans = 0;
        if (n > 2) {
            appear.clear();
            int t = 0;
            for (int i = 2; i < n; i++)
                for (int j = 0; j < wn[i]; j++) {
                    if (appear[w[i][j]]) continue;
                    appear[w[i][j]] = true;
                    once[t++] = w[i][j];
            }
            ans = 0x7fffffff;
            for (int sta = 0; sta < 1 << (n - 2); sta++) {
                for (int i = 0; i < t; i++)
                    unknown[once[i]] = 0;
                for (int i = 2; i < n; i++) {
                    int t = 1 << ((sta >> (i - 2)) & 1);
                    for (int j = 0; j < wn[i]; j++)
                        unknown[ w[i][j] ] |= t;
                }
                int cur = 0;
                for (int k = 0; k < t; k++) {
                    int item = once[k];
                    if (known[item] == 3) continue;
                    if ((known[item] | unknown[item]) == 3) cur++;
                }
                if (cur < ans) ans = cur;
            }
        }
        ans += base;
        printf("Case #%d: %d\n", cas, ans);

    }
    return 0;
}
