/*
 *ID:   Cowboy
 *TASK:
 *Judge:
 */
#include <bits/stdc++.h>
#define INF 0x7fffffff
#define INFLL 1e17
#define PI 2*acos(0.0)
#define show(x) cout<< #x <<" is "<< x <<"\n"
using namespace std;

#define FS first
#define SC second
#define PB(t) push_back(t)
#define ALL(t) t.begin(),t.end()
#define MP(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))

typedef pair<int, int> II;
typedef vector<int> VI;
typedef vector<II> VII;

unsigned long long mypow(unsigned long long k, unsigned long long c) {
    unsigned long long res = 1;
    for (int i = 0 ; i < c; i++) {
        res *= k;
    }
    return res;
}

void solve(int c, int k, int s) {
    if (k == 1) {
        cout<<1;
        return;
    }
    if (c == 1){
        if (s == k) {
            cout<<1;
            for (int i= 2; i <= k; i++) {
                cout<<" "<<i;
            }
        } else {
            cout<<"IMPOSSIBLE";
        }
        return;
    }
    if (s <= k/2) {
        cout<<"IMPOSSIBLE";
        return;
    }
    if(s == k){
        cout<<1;
        for (int i= 2; i <= k; i++) {
            cout<<" "<<i;
        }
        return ;
    }

    unsigned long long idx=2, kc = mypow(k,c-1);
    cout<<idx;
    for (int i = 1; i <s; i++) {
        idx += kc+2;
        if(idx >= kc+k){
            cout<<" "<<kc+k;
            break;
        }
        cout<<" "<<idx;
    }
}

int main( ){
#ifndef ONLINE_JUDGE
   freopen("D-small-attempt1.in", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif
    int T, c, k, s;
    cin>>T;
    string str;
    for (int cas = 0; cas < T; cas++) {
        cin>>k>>c>>s;
        cout<<"Case #"<<cas+1<<": ";
        solve(c, k, s);
        cout<<"\n";
    }
return 0;
}
