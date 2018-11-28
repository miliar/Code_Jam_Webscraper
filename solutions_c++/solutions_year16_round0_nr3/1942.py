#include <bits/stdc++.h>

#define INF (1 << 29)
#define rep2(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) rep2(i,0,n)
#define EPS 1e-10

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

int main()
{
    cout << "Case #1:" << endl;
    rep(i,500){
        string str;
        vector<ll> ans(9);
        cin >> str;
        rep(j,9) cin >> ans[j];

        cout << str << str << ' ';
        rep(j,8) cout << ans[j] << ' ';
        cout << ans[8] << endl;
    }
    return 0;
}

