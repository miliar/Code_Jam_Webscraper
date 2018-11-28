#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <sstream>

using namespace std;

bool check(bool seen[]){
  for(int i=0;i<10;i++){
    if(seen[i] == false) return false;
  }
  return true;
}

int main(void){
  int T;
  long long itr, n, last;
  cin >> T;
  int N[T+1];
  bool seen[10];
  string res;
  ostringstream stream;

  for(int i=1;i<=T;i++){
    cin >> N[i];
  }

  for(int i=1;i<=T;i++){
    cout << "Case #" << i << ": ";
    for(int j=0;j<10;j++){
      seen[j] = false;
    }
    itr = 1;
    if(N[i] == 0){
      cout << "INSOMNIA" << endl;
      continue;
    }
    else{
      while(!check(seen)){
        n = N[i]*itr;
        last = N[i]*itr;
        do{
          seen[n%10] = true;
          n /= 10;
        }while(n != 0);
        itr++;
      }
      cout << last << endl;
    }
  }

  return 0;
}
