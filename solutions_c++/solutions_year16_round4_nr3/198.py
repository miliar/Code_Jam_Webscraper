#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> love;
string t;
bool ready;

bool bej[1000];
int komp;
set<int> jo;
vector<int> k[1000];
    vector<int> g[1000];

void dfs(int x) {
    bej[x]=true;
    if (jo.find(x)!=jo.end()) {
        k[komp].push_back(x);
    }
    for (int sz:g[x]) if (!bej[sz]) dfs(sz);
}

bool ell() {
    for (int i=0;i<1000;i++) {bej[i]=false; k[i].clear(); g[i].clear();}
    for (int i=0;i<n*m;i++) {
        if (t[i]==' ') {
            for (int aa=0;aa<4;aa++) {
                for (int bb=0;bb<4;bb++) g[4*i+aa].push_back(4*i+bb);
            }
        }
        if (t[i]=='\\') {
            g[4*i+0].push_back(4*i+1);
            g[4*i+1].push_back(4*i+0);
            g[4*i+2].push_back(4*i+3);
            g[4*i+3].push_back(4*i+2);
        }
        if (t[i]=='/') {
            g[4*i+0].push_back(4*i+3);
            g[4*i+3].push_back(4*i+0);
            g[4*i+2].push_back(4*i+1);
            g[4*i+1].push_back(4*i+2);
        }

        if (i>=m) {
            g[4*i+0].push_back(4*(i-m)+2);
            g[4*(i-m)+2].push_back(4*i+0);
        }
        if (i+m<n*m) {
            g[4*i+2].push_back(4*(i+m)+0);
            g[4*(i+m)+0].push_back(4*i+2);
        }
        if (i%m>0) {
            g[4*i+3].push_back(4*(i-1)+1);
            g[4*(i-1)+1].push_back(4*i+3);
        }
        if (i%m<m-1) {
            g[4*i+1].push_back(4*(i+1)+3);
            g[4*(i+1)+3].push_back(4*i+1);
        }
    }

    komp=0;
    for (int i=0;i<love.size();i++) {
        int x = love[i];
        if (!bej[x]) {
            dfs(x);
            if (k[komp].size()!=2) {
                return false;
            }
            if (k[komp][1]!=love[i+1]) {
                return false;
            }
            komp++;
        }
    }
    return true;
}

void rek(int l) {
    if (ready) return;
    if (l==n*m) {
        if (ell()) {
            for (int i=0;i<n;i++){
                for (int j=0;j<m;j++) {
                    cout << t[i*m+j];
                }
                cout << endl;
            }
            ready=true;
        }
        return;
    }

    t[l]='\\';
    rek(l+1);
    t[l]='/';
    rek(l+1);
}

void solve()
{
    jo.clear();
    t="";
    cin >> n>>m;
    love.clear();
    ready=false;
    for (int i=0;i<2*(n+m);i++) {
        int x;
        cin >> x;
        love.push_back(x);
    }

    for (int i=0;i<love.size();i++) {
        int x=love[i];
        if (x<=m) {x=(x-1)*4+0; goto aaaa;}
        if (x>m && x<=n+m) {x=((x-m-1)*m+(m-1))*4+1; goto aaaa;}
        if (x>n+m && x<=n+2*m) {x=((m-(x-n-m))+(n-1)*m)*4+2; goto aaaa;}
        if (x>n+2*m) {x=((n-(x-n-2*m))*m)*4+3; goto aaaa;}
        aaaa:
        jo.insert(x);
        love[i]=x;
    }


    for (int i=0;i<n*m;i++) t+='.';
    rek(0);
}

int main()
{
  freopen("C-small-attempt1 (2).in", "r", stdin);
  freopen("C.out", "w", stdout);
  ios_base::sync_with_stdio(false);

  int test;
  cin >> test;
  for (int t = 1;t<=test;t++) {
        cerr<<t<<endl;
    cout << "Case #" << t<<": "<<endl;
    solve();
    if (!ready) cout << "IMPOSSIBLE";
    cout << endl;
  }

  return 0;
}
