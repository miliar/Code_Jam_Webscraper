#include <iostream>
#include <vector>
using namespace std;

int main(){
  int kase;
  cin >> kase;
  int k = 0;
  while(k < kase){
    int a, b, c;
    cin >> a >> b >> c;
    cout<<"Case #"<<(k+1)<<":";
    for(int i=1; i<=a; i++){
      cout<<" "<<i;
    }
    cout<<endl;
    k++;
  }
  return 0;
}
