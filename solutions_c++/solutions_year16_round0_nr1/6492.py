#include <iostream>

using namespace std;

bool allSeen(bool seen[]){
  for(int i = 0; i < 10; i++){
    if(!seen[i]) return false;
  }
  return true;
}
int main(){
  int t;
  cin >> t;
  for(int i = 0; i < t; i++){
    int n;
    cin >> n;
    cout << "Case #" << i+1 << ": ";
    if(n == 0){
      cout << "INSOMNIA" << endl;
    }
    else{
      bool seen[10];
      for(int i = 0; i < 10; i++){
        seen[i] = false;
      }
      int tot = 0;
      while(!allSeen(seen)){
        tot += n;
        int x = tot;
        while(x != 0){
          seen[x%10] = true;
          x/=10;
        }
      }
      cout << tot << endl;
    }
  }
  return 0;
}
