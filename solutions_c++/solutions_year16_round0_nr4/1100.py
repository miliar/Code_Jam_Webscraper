#include <iostream>
using namespace std;


int main() {
  int T, cas, K, C, S;

  cin>>T;
  for (cas=1; cas<=T; ++cas) {
    cout<<"Case #"<<cas<<":";
    cin>>K>>C>>S;
    for (int i=1; i<=K; ++i)
      cout<<' '<<i;
    cout<<endl;
  }

  return 0;
}
