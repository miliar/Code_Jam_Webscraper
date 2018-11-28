#include<bits/stdc++.h>

using namespace std;
#define reps(i,j,k) for(int i = (j); i <= (k); ++i)
#define rep(i,j) reps(i,0,int(j)-1)
#define all(X) (X).begin(),(X).end()
#define rall(X) (X).rbegin(),(X).rend()
#define eb emplace_back
#define rrep(X,Y) for(int (X) = (Y)-1; (X) >=0; --(X))
#define X first
#define Y second
#define in(i,j,k) ((i)>=(j)&&(i)<=(k))
#define sz size()

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

int main(){
  int t;
  string s;
  cin >> t;
  reps(i,1,t){
    cin >> s;
    int ans = 0;
    rep(j, s.sz){
      if(j == s.sz -1)
        ans += s[j] == '-';
      if(j)
        ans+= s[j] != s[j-1];
    }
    bool flag;
    printf("Case #%d: %d\n", i, ans);
  }
  return 0;
}
