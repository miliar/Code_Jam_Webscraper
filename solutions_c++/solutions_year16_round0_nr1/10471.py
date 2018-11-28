#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <set>
#include <queue>
#include <map>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <deque>

using namespace std;
const long double eps = 1e-12;

typedef long long ll;
typedef pair<int , int> pt;

#define sz(a) ((int) a.size() )
#define LL(x) (x << 1)
#define RR(x) ((x << 1) | 1)
#define For(i , a , b) for (int i = a ; i <= b ; i++)
#define Ford(i , a , b) for (int i = a ; i >= b ; i--)
#define Rep(i , n) for (int i = 0 ; i < n ; i++)


void ReadData() {

}

deque<int> de;
vector<int> res;

void Process(int test) {
    int n; cin >> n;
    if (!n) {
        cout << "Case #" << test << ": INSOMNIA" << "\n";
        return;
    }
    bool col[13];
    memset(col , false , sizeof(col));
    int x = n;
    while (true) {
        int z = x;
        while (z) {
            col[z % 10] = true;
            z /= 10;
        }
        bool ok = true;
        Rep(i , 10) if (!col[i]) {ok = false; break; }
        if (ok) {
            cout << "Case #" << test << ": " << x << "\n";
            return;
        }
        x += n;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("input.inp" , "r" , stdin);
    freopen("out.out" , "w" , stdout);
    int test; cin >> test;
    For(i , 1 , test) {
        Process(i);
    }
}
