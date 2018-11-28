// just count the number of inversions
#include <iostream>
using namespace std;

int main(){
  int t;
  string tmp;
  cin >> t;
  for(int i=0;i<t;i++){
    cin >> tmp;
    tmp = tmp + '+';
    int cnt = 0;
    for(int j=0;j<tmp.size()-1;j++){
      if(tmp[j]!=tmp[j+1])cnt++;
    }
    cout << "Case #" << (i+1) << ": " << cnt << endl;
  }
}
