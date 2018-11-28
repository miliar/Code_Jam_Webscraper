#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;

const int N = 4e5 + 5;
int n;
string s;

int getr(){
  int r = 0;
  for(int i = 0; i < n; i++){
    if(s[i] == s[0])
      r++;
    else{
      break;
    }
  }
  return r - 1;
}

void flip(int l, int r){
  for(int i = l; i <= r; i++){
    if(s[i] == '+') s[i] = '-';
    else s[i] = '+';
  }
}

int main(){
  ios::sync_with_stdio(false); cin.tie(0);
  int t;
  cin >> t;
  int cs = 0;
  while(t--){
    cs++;
    cin >> s;
    cout <<"Case #" << cs << ": ";
    n = s.length();
    int ans = 0;
    while(true){
      int r = getr();
      if(s[0] == '+' and r == n - 1) break;
      else{
        flip(0, r);
        ans++;
      }
    }
    cout << ans << endl;
  }
  return 0;
}
