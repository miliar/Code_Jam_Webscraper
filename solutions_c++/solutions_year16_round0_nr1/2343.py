#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;

const int N = 4e2 + 5;
int cnt[N];

bool check(){
  for(int i = '0'; i <= '9'; i++){
      if(cnt[i] == 0) return false;
  }
  return true;
}

int main(){
  ios::sync_with_stdio(false); cin.tie(0);
  int t;
  cin >> t;
  int cs = 0;
  while(t--){
    cs++;
    int n;
    cin >> n;
    cout <<"Case #" << cs << ": ";
    if(n == 0){
      cout << "INSOMNIA" << endl;
      continue;
    }

    int i = 1;
    int ans = 0;
    while(true){
      int tmp = n * i;
      string s = to_string(tmp);
      for(int i = 0; i < s.length(); i++) cnt[s[i]]++;

      if(check()){
        ans = tmp;
        break;
      }
      i++;
    }
    cout << ans << endl;
    for(int i = '0'; i <= '9'; i++) cnt[i] = 0;
  }
  return 0;
}
