#include <bits/stdc++.h>
using namespace std;
 
typedef pair<int,int> pii;
typedef long long ll;

void fastStream(){cin.tie(0);std::ios_base::sync_with_stdio(0);}

int D;
int P[1001];
int main(){
  fastStream();
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    cin>>D;
    for(int i=0;i<D;i++)cin>>P[i];
    int res = 1<<29;
    for(int j = 1; j <= 1000; j++){
      int tmp = 0;
      for(int i=0;i<D;i++){
        tmp += (P[i] + j - 1) / j - 1;
      }
      res = min(res, tmp + j);
    }
    cout<<res<<endl;
  }
  
  return 0;
}
