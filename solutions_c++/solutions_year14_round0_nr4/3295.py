#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

#define D(x) cout << #x << " = " << x << endl;
#define rep(i,a,b) for(int i=a;i<b;i++)
#define repd(i,a,b) for(int i=b-1;i>=a;i--)
#define REP(i,n) rep(i,0,n)
#define REPD(i,n) repd(i,0,n)
#define pb push_back
#define mp make_pair

typedef long long int lld;
typedef vector<int> vi;
typedef vector<lld> vlld;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

int main(){ IO;
  freopen("D.in","r",stdin);
  freopen("D.out","w",stdout);

  int t;
  cin >> t;

  rep(ncase,1,t+1){
    cout << "Case #" << ncase << ": ";

    int n;
    cin >> n;
    vector<double> naomi(n), ken(n);
    REP(i,n) cin >> naomi[i];
    REP(i,n) cin >> ken[i];

    sort(naomi.begin(),naomi.end(),greater<double>());
    sort(ken.begin(),ken.end(),greater<double>());

    int dw = 0;
    rep(k,1,n+1){
      bool good = true;
      REP(i,k) if(naomi[i] < ken[n-k+i]) good = false;
      if(good) dw = k;
    }

    int w = 0;
    int i = 0, j = 0, cnt = 0;
    while(i < n and j < n){
      if(naomi[i] > ken[j]){
        i++;
        if(cnt == 0) w++;
        else cnt--;
      }else{
        j++;
        cnt++;
      }
    }
    cout << dw << " " << w << endl;
  }

  return 0;
}
