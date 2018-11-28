#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}


ll is_prime(ll n){
  for(ll i = 2; i * i <= n; i++){
    if(n % i == 0){
      return i;
    }
  }
  return -1;
}

void small(int N, int J){
  int cnt = 0;
  for(int mask = 0; mask < (1 << N); mask++){
    // 最上位と最下位ビットが1
    if((mask % 2) && ((mask >> (N - 1)) & 1)){
      vector<int> val;
      for(int base = 2; base <= 10; base++){
        ll mul = 1;
        ll num = 0;
        for(int i = 0; i < N; i++){
          if((mask >> i) & 1){
            num += mul;
          }
          mul *= base;
        }
        ll v = is_prime(num);
        if(v != -1){
          val.push_back(v);
        }
      }
      // 答え
      if(val.size() == 9){
        cout<<bitset<16>(mask)<<" ";
        for(int i=0;i<(int)val.size();i++){
          cout<<val[i];
          if(i==(int)val.size()-1)cout<<endl;
          else cout<<" ";
        }
        cnt++;
        if(cnt == J)break;
      }
    }
  }
}

int main(){
  fastStream();
  int T;
  int N, J;
  cin >> T;
  for(int t=1;t<=T;t++){
    cout << "Case #" << t << ":"<<endl;
    cin>>N>>J;
    small(N, J);
  }
  
  return 0;
}
