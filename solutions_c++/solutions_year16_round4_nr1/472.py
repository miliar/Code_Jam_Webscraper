#include <bits/stdc++.h>
using namespace std;

int n, r, p, s;
string sol[30][300];

void solve()
{
    cin >> n>>r>>p>>s;

    sol[0]['R'] = "R";
    sol[0]['P'] = "P";
    sol[0]['S'] = "S";

    for (int i=1;i<=n;i++) {
        sol[i]['R'] = (sol[i-1]['R']<sol[i-1]['S']) ?  sol[i-1]['R']+sol[i-1]['S'] : sol[i-1]['S']+sol[i-1]['R'];
        sol[i]['P'] = (sol[i-1]['P']<sol[i-1]['R']) ?  sol[i-1]['P']+sol[i-1]['R'] : sol[i-1]['R']+sol[i-1]['P'];
        sol[i]['S'] = (sol[i-1]['P']<sol[i-1]['S']) ?  sol[i-1]['P']+sol[i-1]['S'] : sol[i-1]['S']+sol[i-1]['P'];
    }

    vector<string> soll;
    soll.push_back(sol[n]['R']);
    soll.push_back(sol[n]['P']);
    soll.push_back(sol[n]['S']);

    bool bb=false;
    for (string x:soll) {
        int rr, pp, ss;
        rr=0;
        pp=0;
        ss=0;
        for (char y : x) {
            if (y=='R') rr++;
            if (y=='P') pp++;
            if (y=='S') ss++;
        }
        if ((rr==r) && (pp==p) && (ss==s)) {
            cout << x;
            bb=true;
            return;
        }
    }

    if (!bb) {
        cout << "IMPOSSIBLE";
    }
}

int main()
{
  freopen("A-large (3).in", "r", stdin);
  freopen("A.out", "w", stdout);
  ios_base::sync_with_stdio(false);

  int test;
  cin >> test;
  for (int t = 1;t<=test;t++) {
    cout << "Case #" << t<<": ";
    solve();
    cout << endl;
  }

  return 0;
}
