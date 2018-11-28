#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

#define FOR(i,a,b) for(int i = (a); i <= (b);i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define oo 1000000009
using namespace std;

#define maxn 2000
int n, a[maxn];
vector<int> p;

void solve() {
    p.clear();
    FOR(i,1,n) p.push_back(a[i]);
    int total = 0;
    FOR(iter,1,n) {
        int min_val = oo, u = -1;
        FR(j,p.size()) 
        if (p[j] < min_val) {
            min_val = p[j];
            u = j+1;
        }
        int T = p.size();
        total += min(u-1, T-u);
        u--;
        FOR(j,u,T-2) {
            swap(p[j], p[j+1]);
        }
        p.pop_back();
    }
    cout << total << endl;
}
int main() 
{
    freopen("BB4.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> n;
        FOR(i,1,n) cin >> a[i];
        solve();
    }    
    return 0;
}

