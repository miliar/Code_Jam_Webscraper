#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cctype>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>

#define REP(i,n) for(int i=0;i<(n);i++)
#define TR(i,x) for(__typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))
#define SIZE(x) (int)(x).size()

#define MP make_pair
#define PB push_back

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

string Get(char x, bool flag) {
    if (x == 'R') {
        return "RS";
    } else if (x == 'P') {
        return "PR";
    } else {
        return "SP";
    }
}

char s[2][10000];

string GetString(char ch, int N) {
    char* crt = s[0];
    char* nxt = s[1];
    crt[0] = ch;
    for (int i = 0; i < N; ++i) {
        int L = 1 << i;
        REP(j, L) {
            string t = Get(crt[j], i < N - 1); 
            nxt[j << 1] = t[0];
            nxt[j << 1 | 1] = t[1];
        }
        swap(crt, nxt);
    }
    string ret = "";
    REP(i, 1 << N)  {
        ret += crt[i];
    }
    int L = 1 << N;
    for (int i = 0; i < N; ++i) {
        string tmp = "";
        for (int j = 0; j < L; j += 1 << i + 1) {
            string A = "";
            REP(k, 1 << i) {
                A += ret[j + k];
            }
            string B = "";
            REP(k, 1 << i) {
                B += ret[j + (1 << i) + k];
            }
            if (A > B) swap(A, B);
            tmp += A;
            tmp += B;
        }
        ret = tmp;
    }
    return ret; 
}

bool Check(string str, int R, int P, int S) {
    TR(it, str) {
        if (*it == 'R') {
            --R;
            if (R < 0) return false;
        } else if (*it == 'P') {
            --P;
            if (P < 0) return false;
        } else {
            --S;
            if (S < 0) return false;
        }
    }
    return true;
}

void Solve() {
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    vector<string> ans;
    ans.PB(GetString('R', N));
    ans.PB(GetString('P', N));
    ans.PB(GetString('S', N));
    SORT(ans);
    bool flag = false;
    REP(i, 3) {
        if (Check(ans[i], R, P, S)) {
            cout << ans[i] << endl;
            flag = true;
            break;
        }
    }
    if (!flag) {
        puts("IMPOSSIBLE");
    }
}

int main() {
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
    int cas;
    cin >> cas;
    for (int T = 1; T <= cas; ++T) {
        printf("Case #%d: ", T);
        Solve();
        cerr << "Case #" << T << ": done!" << endl;
    }
    return 0;
}

