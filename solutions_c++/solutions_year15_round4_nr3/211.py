#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <set>
#include <map>

using namespace std;

const int MAXN = 5000;

int eng[MAXN], fre[MAXN];
int n, all_cnt;
vector< vector< int > > g;
map< string, int > mp;

int
get_cnt()
{
    int res = 0;
    for (int i = 0; i < all_cnt; ++i) {
        if (eng[i] && fre[i]) {
            ++res;
        }
    }
    return res;
}

inline int
inc_val(int *f, int *s, int pos)
{
    f[pos]++;
    return (f[pos] == 1 && s[pos]);
}

inline int
dec_val(int *f, int *s, int pos)
{
    f[pos]--;
    return (f[pos] == 0 && s[pos]);
}

int
rec(int pos, int ans)
{
    if (pos == n) {
        return ans;
    }
    // english
    for (auto val : g[pos]) {
        ans += inc_val(eng, fre, val);
    }
    int res = rec(pos + 1, ans);
    for (auto val : g[pos]) {
        ans -= dec_val(eng, fre, val);
        ans += inc_val(fre, eng, val);
    }
    res = min(res, rec(pos + 1, ans));
    for (auto val : g[pos]) {
        ans -= dec_val(fre, eng, val);
    }
    return res;
}

void
process(int id)
{
    scanf("%d\n", &n);
    g.assign(n, vector< int >());
    mp.clear();
    char buf[15000];
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        fgets(buf, 14000, stdin);
        int beg = 0, len = strlen(buf);
        if (buf[len - 1] == '\n') {
            buf[--len] = '\0';
        }
        while (beg < len) {
            int en = beg;
            while (isalpha(buf[en])) ++en;
            buf[en] = '\0';
            string tmp(buf + beg);
            // fprintf(stderr, "%s_", tmp.data());
            auto it = mp.find(tmp);
            if (it == mp.end()) {
                it = mp.insert(make_pair(tmp, cnt)).first;
                eng[cnt] = fre[cnt] = 0;
                ++cnt;
            }
            int id = it->second;
            g[i].push_back(id); 
            beg = en + 1;
        }
        /*fprintf(stderr, "\n");
        fflush(stderr);*/
    }
    int res = 0;
    for (auto val : g[0]) {
        res += inc_val(eng, fre, val);
    }
    for (auto val : g[1]) {
        res += inc_val(fre, eng, val);
    }
    res = rec(2, res);
    printf("Case #%d: %d\n", id, res);
}

int
main()
{
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        process(i);
    }
    return 0;
}
