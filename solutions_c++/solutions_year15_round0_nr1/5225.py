#include <bits/stdc++.h>
using namespace std;

const int N = 1000;

int main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    string str;
    int n, v[N+1], ans = 0, sum = 0;

    cin >> n >> str;
    for(int i=0;i<str.size();i++){
      v[i] = str[i] - '0';
    }

    for(int i=0;i<=n;i++){
      if(v[i] > 0) {
        ans += max(0, i - sum);
        sum += max(0, i - sum);
      }
      sum = (sum + v[i]) % (N+2);
    }

    cout << "Case #" << t << ": " << ans << endl;
  }
}
