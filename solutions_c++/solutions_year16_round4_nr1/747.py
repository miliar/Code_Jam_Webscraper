#include <bits/stdc++.h>
#define MAXN 11234

using namespace std;

int N, R, P, S, T;

map <char, char> killMap;
map <char, int> mapInt;
string ans;

char nowAlpha[MAXN];

string f[20][5];

void updateAnsString(char ch) {
    int nowN = 1;
    int cnt[3];
    memset(cnt, 0, sizeof(cnt));
    nowAlpha[0] = ch;
    for (; nowN < 1 << N; nowN <<= 1) {
        for (int i = nowN - 1; i >= 0; --i) {
            nowAlpha[i * 2 + 1] = killMap[nowAlpha[i]];
            nowAlpha[i * 2] = nowAlpha[i];
        }
    }
    for (int i = 0; i < nowN; ++i) {
        cnt[mapInt[nowAlpha[i]]]++;
    }
    if (P != cnt[mapInt['P']]) return;
    if (R != cnt[mapInt['R']]) return;
    if (S != cnt[mapInt['S']]) return;
    if (ans == "IMPOSSIBLE") ans = f[N][mapInt[ch]];
    else ans = min(ans, f[N][mapInt[ch]]);
}

void initF() {
    f[0][mapInt['P']] = "P";
    f[0][mapInt['R']] = "R";
    f[0][mapInt['S']] = "S";
    for (int i = 1; i <= 12; ++i) {
        int u = mapInt['P'], v = mapInt[killMap['P']];
        f[i][u] = min(f[i - 1][u] + f[i - 1][v], f[i - 1][v] + f[i - 1][u]);
        string tmp = f[i][u];
        u = mapInt['R'], v = mapInt[killMap['R']];
        f[i][u] = min(f[i - 1][u] + f[i - 1][v], f[i - 1][v] + f[i - 1][u]);
        
        u = mapInt['S'], v = mapInt[killMap['S']];
        f[i][u] = min(f[i - 1][u] + f[i - 1][v], f[i - 1][v] + f[i - 1][u]);
    }
}
int main() {
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    killMap['P'] = 'R';
    killMap['R'] = 'S';
    killMap['S'] = 'P';
    mapInt['P'] = 0;
    mapInt['R'] = 1;
    mapInt['S'] = 2;
    initF();
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d%d%d", &N, &R, &P, &S);
        ans = "IMPOSSIBLE";
        updateAnsString('P');
        updateAnsString('R');
        updateAnsString('S');
        cout << "Case #" << ca << ": " << ans << endl;
    }
    return 0;
}