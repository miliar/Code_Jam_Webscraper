#include <iostream>
using namespace std;

int main(){
  int cases;
  cin >> cases;
  for(int i = 1; i< cases+1; i++){
    int k, c, s;
    cin >> k >> c >> s;
    cout << "Case #" << i <<": ";
    for(int q=1; q<s+1; q++){
      cout << q << " ";
    }
    cout << endl;
  }
}
