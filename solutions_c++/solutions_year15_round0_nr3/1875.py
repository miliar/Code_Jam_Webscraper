#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <cmath>
#include <cstdio>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

#pragma comment(linker, "/STACK:1024000000,1024000000")

#define     IT              iterator
#define     PB(x)           push_back(x)
#define     CLR(a,b)        memset(a,b,sizeof(a))

using namespace std;

typedef     long long               ll;
typedef     unsigned long long      ull;
typedef     vector<int>             vint;
typedef     vector<ll>              vll;
typedef     vector<ull>             vull;
typedef     set<int>                sint;
typedef     set<ull>                sull;

const int maxn = 10000 + 5;
int l,x;
int len;
int g[5][5];
char s[maxn];
int dij[maxn];

void init() {
    g[1][1] = 1; g[1][2] = 2;  g[1][3] = 3;  g[1][4] = 4;
    g[2][1] = 2; g[2][2] = -1; g[2][3] = 4;  g[2][4] = -3;
    g[3][1] = 3; g[3][2] = -4; g[3][3] = -1; g[3][4] = 2;
    g[4][1] = 4; g[4][2] = 3;  g[4][3] = -2; g[4][4] = -1;
}

int idx(char x) {
    if (x == 'i') return 2;
    else if (x == 'j') return 3;
    else if (x == 'k') return 4;
}

bool check_k(int pos) {
    int signal = 1;
    int ans = 1;
    for (int i = pos; i < len; i++) {
        if (g[ans][dij[i]] < 0) signal *= -1;
        ans = abs(g[ans][dij[i]]);
    }
    if (ans == 4 && signal == 1) return true;
    return false;
}

bool check_j(int pos) {
    int signal = 1;
    int ans = 1;
    for (int i = pos; i < len; i++) {
        if (g[ans][dij[i]] < 0) signal *= -1;
        ans = abs(g[ans][dij[i]]);
        //if (ans == 3 && signal == 1) cout<<"j "<<i<<endl;
        if (ans == 3 && signal == 1 && check_k(i+1)) return true;
    }
    return false;
}

bool check_i(int pos) {
    int signal = 1;
    int ans = 1;
    for (int i = pos; i < len; i++) {
        if (g[ans][dij[i]] < 0) signal *= -1;
        ans = abs(g[ans][dij[i]]);
        //if (ans == 2 && signal == 1) cout<<"i "<<i<<endl;
        if (ans == 2 && signal == 1 && check_j(i+1)) return true;
    }
    return false;
}

int main() {
    init();
    int T;
    cin>>T;
    for (int t = 1; t <= T; t++) {
        cin>>l>>x;
        scanf("%s",s);
        string ss = "";
        for (int i = 0; i < x; i++) ss += s;
        len = ss.length();
        for (int i = 0; i < len; i++) dij[i] = idx(ss[i]);
        if (check_i(0)) {
            printf("Case #%d: YES\n",t);
        }
        else printf("Case #%d: NO\n",t);
    }
}
