#include <vector>
#include <string>
#include <iostream>
#include <set>
using namespace std;

int main() {
  int tests;
  cin>>tests;
  for(int i=0;i<tests;i++) {
    int K,C,S;
    cin>>K>>C>>S;
    cout<<"Case #"<<(i+1)<<":";
    for(int j=1;j<=K;j++) cout<<" "<<j; cout<<endl;
  }
  return 0;
}
