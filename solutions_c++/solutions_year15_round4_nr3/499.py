#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define MP make_pair
#define PB push_back
#define FORE(it,c) for(__typeof(c.begin())it=c.begin();it!=c.end();it++)
typedef pair<int,int> pii;

const int maxN = 211, maxW = 14, maxL = 4044;

int n, test;
int L[maxN][maxW], nl[maxN];
int lang[maxL], lx[maxL];
map<string, int> ma;
int nw;

int getid(string s){
    if (ma.count(s)) return ma[s];
    ma[s] = ++nw;
    return nw;
}

void readLine(int i){
    i -= 2;
    if (i >= 0) nl[i] = 0;
    char c, s[20];
    do{
        scanf("%s%c", s, &c);
        int id = getid(string(s));
        //printf("%d, %d = %s\n", i, id, s);
        if (i >= 0) L[i][nl[i]++] = id;
        else if (i == -2) lang[id] |= 1;
        else if (i == -1) lang[id] |= 2;
    } while (c == ' ');
}

void solve(){
    scanf("%d", &n);
    memset(lang, 0, sizeof lang);
    ma.clear();
    nw = 0;
    for (int i = 0; i < n; i++) readLine(i);
    n -= 2;
    int p, res = nw;
    for (int s = 0; s < (1 << n); s++){
        memset(lx, 0, sizeof lx);
        for (int i = 0; i < n; i++){
            if ((s >> i) & 1) p = 1; //English
            else p = 2; //French
            for (int j = 0; j < nl[i]; j++) lx[L[i][j]] |= p;
        }
        int all = 0;
        for (int i = 1; i <= nw; i++)
            all += ((lang[i]|lx[i]) == 3);
        res = min(res, all);
    }
    printf("%d\n", res);
}

int main(){
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int t; scanf("%d", &t);
    for (test = 1; test <= t; test++){
        printf("Case #%d: ", test);
        solve();
    }
    return 0;
}
