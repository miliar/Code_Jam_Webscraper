#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}


int main(){
  fastStream();
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    cout << "Case #" << t << ": ";
    ll N;
    cin>>N;
    if(N==0){
      cout<<"INSOMNIA"<<endl;
      continue;
    }
    bool used[10] = {};
    for(ll i=1;;i++){
      ll a = N*i;
      while(a){
        used[a%10] = true;
        a /= 10;
      }
      bool ok = true;
      for(int j=0;j<10;j++){
        if(!used[j]){
          ok = false;
        }
      }
      if(ok){
        cout<<N*i<<endl;
        break;
      }
    }
  }
  
  return 0;
}
