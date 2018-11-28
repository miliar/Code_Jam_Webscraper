#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<long double> score;

vector<long double> s;

long double d[203][203];

long double maxi;

void doit() {
    d[0][0]=1.0;
    d[0][1]=0.0;
    for (int i=1;i<=k;i++) {
        for (int y=0;y<=i;y++) {
            d[i][y]=0.0;
            if (y>0) {
                d[i][y]+=d[i-1][y-1]*s[i-1];
            }
            d[i][y]+=d[i-1][y]*(1.0-s[i-1]);
        }
    }

    if (d[k][k/2]>maxi) maxi=d[k][k/2];
}

void solve()
{
    cin >> n>> k;
    score.clear();
    for (int i=0;i<n;i++) {
        long double ld;
        cin >> ld;
        score.push_back(ld);
    }

    sort(score.begin(), score.end());

    maxi=0.0;
    for (int i=0;i<=k;i++) {
        s.clear();
        for (int j=0;j<i;j++) {
            s.push_back(score[j]);
        }
        int j=n-1;
        while (s.size()<k) {
            s.push_back(score[j]);
            j--;
        }
        doit();
    }

    cout << fixed << maxi;

}

int main()
{
  freopen("B-large (2).in", "r", stdin);
  freopen("B.out", "w", stdout);
  ios_base::sync_with_stdio(false);

  cout.precision(7);

  int test;
  cin >> test;
  for (int t = 1;t<=test;t++) {
    cout << "Case #" << t<<": ";
    solve();
    cout << endl;
  }

  return 0;
}
