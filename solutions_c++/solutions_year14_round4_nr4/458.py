#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <algorithm>
 
#include <cassert>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

typedef long long ll;

const int modulo = 1e9 + 7;

const int max_s = 11;
const int max_m = 8;
const int max_n = 4;
const int max_c = 26;
const int max_t = max_s * max_m;

int m, n;
char s[max_m][max_s];
int slen[max_m];
int sv[max_m];
int c[max_n];
int ans_val, ans_cnt;

struct trie
{
    int nx[max_c];
};

trie t[max_t];
int lt;

void init_trie(int id)
{
    for (int i = 0; i < max_c; ++i) t[id].nx[i] = -1;
}

int trie_size(int id)
{
    int ans = 1;
    for (int i = 0; i < max_c; ++i)
        if (t[id].nx[i] != -1)
            ans += trie_size(t[id].nx[i]);
    return ans;
}

void add_to_trie(int id, char* s, int len, int pos) 
{
    if (pos == len) return ;
    int& v = t[id].nx[s[pos] - 'A'];
    if (v == -1) {
        v = lt;
        init_trie(lt);
        ++lt;
    }
    add_to_trie(v, s, len, pos + 1);
}

int root[max_n];

void check()
{
    for (int i = 0; i < n; ++i) c[i] = 0;
    for (int i = 0; i < m; ++i) ++c[sv[i]];
    for (int i = 0; i < n; ++i) if (c[i] == 0) return;
    lt = 0;
    for (int i = 0; i < n; ++i) {
        root[i] = lt;
        init_trie(lt);
        ++lt;
    }
    for (int i = 0; i < m; ++i)
        add_to_trie(root[sv[i]], s[i], slen[i], 0);
    int cans_val = 0;
    for (int i = 0; i < n; ++i) {
        cans_val += trie_size(root[i]);
    }
    if (cans_val == ans_val) {
        ++ans_cnt;
    } else if (cans_val > ans_val) {
        ans_val = cans_val;
        ans_cnt = 1;
    }
}

void rec(int v)
{
    if (v == m) {
        check();
        return ;
    }
    for (int i = 0; i < n; ++i) {
        sv[v] = i;
        rec(v + 1);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tests;
    scanf("%d\n", &tests);
    for (int test = 1; test <= tests; ++test) {
        printf("Case #%d: ", test);
        scanf("%d%d\n", &m, &n);
        for (int i = 0; i < m; ++i) {
            scanf("%s\n", s[i]);
            slen[i] = strlen(s[i]);
        }
        ans_val = -1;
        rec(0);
        printf("%d %d\n", ans_val, ans_cnt);
    }
  
    return 0;
}
