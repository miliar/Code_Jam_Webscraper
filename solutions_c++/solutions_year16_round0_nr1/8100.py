#include <iostream>

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int i=0;i<t;i++){
    long long n;
    cout << "Case #" << i+1 << ": ";
    cin >> n;
    bool flag[10] = {};
    bool end = false;
    if(!n){
      cout << "INSOMNIA" << endl;
      end = true;
    }
    int num = n;
    while(!end){
      int mod = n;
      while(mod){
        flag[mod%10] = true;
        mod /= 10;
      }
      bool all = true;
      for(int j=0;j<10;j++){
        if(!flag[j])
          all = false;
      }
      end = all;
      if(!all)
        n += num;
      else
        cout << n << endl;
    }
  }
  return 0;
}
