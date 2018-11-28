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

struct Node {
    int s;
    char x;

    Node() {}
    Node(int s, char x):s(s),x(x) {}

    Node operator * (const Node& a) const {
        Node ret = Node(s * a.s, 0);
        if (x == '1') {
            ret.x = a.x;
        } else if (a.x == '1') {
            ret.x = x;
        } else if (x == a.x) {
            ret.x = '1';
            ret.s *= -1;
        } else {
            int i = x - 'i', j = a.x - 'i';
            if ((i + 1) % 3 != j) {
                ret.s *= -1;
                swap(i, j);
            }
            ret.x = 'i' + (j + 1) % 3;
        }
        return ret;
    }

    bool operator == (const Node& a) const {
        return s == a.s && x == a.x;
    }

    void disp() {
        if (s == -1) cout << "-";
        cout << x <<endl;
    }
} ;

char a[10010];

void Solve() {
    int n, m;
    cin >> n >> m;
    scanf("%s", a);
    LL lpos = 1ll * n * m, rpos = -1;
    Node p(1, '1'), all(1, '1');
    REP(i, n) p = p * Node(1, a[i]);
    REP(i, m % 4) all = all * p;
    if (all == Node(-1, '1')) {
        int tot = n * min(4, m);
        p = Node(1, '1');
        REP(i, tot) {
            p = p * Node(1, a[i % n]);
            if (p == Node(1, 'i')) {
                lpos = i;
                break;
            }
        }
        p = Node(1, '1');
        for (int i = tot - 1; i >= 0; --i) {
            p = Node(1, a[i % n]) * p;
            if (p == Node(1, 'k')) {
                rpos = 1ll * n * m - 1 - (tot - 1 - i); 
                break;
            }
        }
        if (lpos < rpos) {
            puts("YES");
        } else {
            puts("NO");
        }
    } else {
        puts("NO");
    }
}

int main() {
//	freopen("C.in","r",stdin);
//	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
// 	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
// 	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
 	freopen("C-small-attempt3.in","r",stdin);freopen("C-small-attempt3.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
    int cas;
    cin >> cas;
    for (int T = 1; T <= cas; ++T) {
        printf("Case #%d: ", T);
        Solve();
    }
    return 0;
}


