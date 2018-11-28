#include <bits/stdc++.h>
using namespace std;
#define repl(i,a,b) for(int i=(int)(a);i<(int)(b);i++)
#define rep(i,n) repl(i,0,n)
#define mp(a,b) make_pair((a),(b))
#define pb(a) push_back((a))
#define all(x) (x).begin(),(x).end()
#define uniq(x) sort(all(x)),(x).erase(unique(all(x)),end(x))
#define fi first
#define se second
#define dbg(x) cout<<#x" = "<<((x))<<endl
template<class T,class U> ostream& operator<<(ostream& o, const pair<T,U> &p){o<<"("<<p.fi<<","<<p.se<<")";return o;}
template<class T> ostream& operator<<(ostream& o, const vector<T> &v){o<<"[";for(T t:v){o<<t<<",";}o<<"]";return o;}

#define INF 2147483600

int solve(){
  string s;
  int k;
  cin>>s>>k;
  int n = s.size();

  auto flip = [&](string &t, int p){
    repl(j,p,k+p){
      if(t[j]=='-') t[j]='+';
      else t[j]='-';
    }
  };

  int ans = 0;
  rep(i,n-k+1){
    if(s[i]=='-'){
      flip(s, i);
      ans++;
    }
  }
  repl(i,n-k+1,n) if(s[i]=='-') return -1;

  return ans;
}

int main(){
  int t;
  cin>>t;
  rep(i,t){
    int r = solve();
    cout << "Case #" << i+1 << ": ";
    if(r<0) cout << "IMPOSSIBLE";
    else cout << r;
    cout << endl;
  }

  return 0;
}
