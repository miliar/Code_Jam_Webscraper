#include <bits/stdc++.h>
using namespace std;

map< map< int, int, greater<int> >, int> memo;

int solve(map< int, int, greater<int> > &dict) {
    dict.erase(1);
    map< map< int, int, greater<int> >, int>::iterator it = memo.find(dict);
    if (it != memo.end())
        return it->second;
    if (dict.empty())
        return memo[dict] = 1;

    int ret = dict.begin()->first;
    map< int, int, greater<int> > tmp = dict;
    int x = tmp.begin()->first, y = tmp.begin()->second;
    tmp.erase(tmp.begin());

    for (int i = 1; i <= x/2; i++) {
        map< int, int, greater<int> > m = tmp;
        m[i] += y, m[x-i] += y;
        ret = min(ret, solve(m) + y);
    }

    return memo[dict] = ret;
}

int main() {
    int T, D, P;
    map< int, int, greater<int> > dict;

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &D);
        dict.clear();
        for (int i = 0; i < D; i++) {
            scanf("%d", &P);
            dict[P]++;
        }
        memo.clear();
        printf("Case #%d: %d\n", t, solve(dict));
    }
}
