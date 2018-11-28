#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef long double ldb;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

struct trie {
    trie *to[26];
};

trie mem[100500];
int mcnt = 0;

trie *new_trie() {
    forn(i, 26)
        mem[mcnt].to[i] = NULL;
    return &mem[mcnt++];
}

int n, m;
string s[10];

int k[4];

int cnt[1000];

int ans;
int anscnt;

void gen(int num) {
    if (num == m) {
        forn(i, n)
            if (k[i] == 0)
                return;
        int cur = 0;
        forn(i, n)
            cur += cnt[k[i]];
        if (cur > ans) {
            ans = cur;
            anscnt = 0;
        }
        if (cur == ans)
            anscnt++;
        return;
    }
    forn(i, n) {
        k[i] ^= (1 << num);
        gen(num + 1);
        k[i] ^= (1 << num);
    }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d ", &T);
    forn(test, T) {
        printf("Case #%d: ", test + 1);

        scanf(" %d%d ", &m, &n);
        forn(i, m)
            cin >> s[i];

        forn(z, (1 << m)) {
            mcnt = 0;
            trie *root = new_trie();
            forn(i, m)
                if (z & (1 << i)) {
                    trie *cur = root;
                    forn(j, s[i].length()) {
                        int a = s[i][j] - 'A';
                        if (!cur->to[a])
                            cur->to[a] = new_trie();
                        cur = cur->to[a];
                    }
                }

            cnt[z] = mcnt;
        }

        forn(i, n)
            k[i] = 0;
        ans = anscnt = 0;
        gen(0);

        printf("%d %d\n", ans, anscnt);

    }
    return 0;
}
