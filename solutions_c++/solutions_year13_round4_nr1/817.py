#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

#define pb push_back
#define mp make_pair

using namespace std;

typedef long long LL;
typedef pair< LL , LL > PLL;

const LL MOD = 1000002013;

LL n, m;
LL sum;
vector< PLL > les, ris;
vector< PLL > vecLe, vecRi;

LL getSum(LL k) {
    return ((k * (k + 1)) / 2) % MOD;
}

void read() {
    LL a, b, c;
    les.clear();
    ris.clear();

    cin >> n >> m;
    sum = 0;
    for(int i = 0; i < m; i ++) {
        cin >> a >> b >> c;
        sum = (sum + (c * getSum(b - a - 1)) % MOD) % MOD;
        les.pb(mp(a, c));
        ris.pb(mp(b, c));
    }
}

void solve() {
    sort(les.begin(), les.end());
    sort(ris.begin(), ris.end());

    vecLe.clear();
    vecRi.clear();

    LL pos = les[0].first, cnt = les[0].second;
    for(int i = 1; i < les.size(); i ++)
        if(les[i].first == pos) cnt += les[i].second;
        else {
            vecLe.pb(mp(pos, cnt));
            cnt = les[i].second;
            pos = les[i].first;
        }
    vecLe.pb(mp(pos, cnt));

    pos = ris[0].first, cnt = ris[0].second;
    for(int i = 1; i < ris.size(); i ++)
        if(ris[i].first == pos) cnt += ris[i].second;
        else {
            vecRi.pb(mp(pos, cnt));
            cnt = ris[i].second;
            pos = ris[i].first;
        }
    vecRi.pb(mp(pos, cnt));

    LL ans = 0;

    int index = 0;
    while(index < vecRi.size()) {
        int pos;
        for(int i = 0; i < vecLe.size(); i ++) {
            if(vecLe[i].first > vecRi[index].first) break;
            if(vecLe[i].second) pos = i;
        }
        LL br = min(vecRi[index].second, vecLe[pos].second);
        ans = (ans + (br * getSum(vecRi[index].first - vecLe[pos].first - 1)) % MOD) % MOD;
        vecRi[index].second -= br;
        vecLe[pos].second -= br;
        if(vecRi[index].second == 0) index ++;
    }

    cout << (ans - sum + MOD) % MOD << endl;
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i ++) {
        printf("Case #%d: ", i);
        read();
        solve();
    }

    return 0;
}
