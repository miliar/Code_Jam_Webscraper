#include <sstream>
#include <iostream>
#include <cstdio>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <utility>
#include <queue>
#include <deque>
#pragma comment(linker, "/STACK:16777216")

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector< pair<int, int> > vii;

#define foru(i,a,b) for(int i = int(a); i <= int(b); ++i)
#define ford(i,b,a) for(int i = int(b); i >= int(a); --i)
#define rep(i, n) for(int i = 0; i < int(n); ++i)
#define all(a) a.begin(),a.end()
#define size(a) int(a.size())
#define fill(a,x) memset(a, (x), sizeof(a))
#define mp(x,y) make_pair((x), (y))
#define pb(x) push_back((x))
#define fr first
#define sc second
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

int a[1000];

int read() {   int x;   scanf("%d",&x);   return x;   }
int read(int &x) {  scanf("%d",&x);     return x;   }
int readln(int &x) {   scanf("%d\n",&x);   return x;   }

bool is_palin(int n) {
    int m = 0;
    while (n > 0) {
        a[m++] = n%10;
        n /= 10;
    }
    int i = 0, j = m-1;
    while (i < j) {
        if (a[i] != a[j]) return false;
        ++i;    --j;
    }
    return true;
}


int main() {
#ifndef ONLINE_JUDGE
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C.out", "w", stdout);
#endif
    int nTest = read();
    foru(test_id,1,nTest) {
        int a = read(), b = read(), res = 0;
        foru(i,1,b) if (is_palin(i)) {
            int j = i*i;
            if (j > b) break;
            if (j < a) continue;
            if (is_palin(j)) ++res;
        }
        printf("Case #%d: %d\n",test_id,res);
    }
    return 0;
}
