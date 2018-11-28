#include <iostream>
#include <string>
using namespace std;

int main(){
  int cases;
  cin >> cases;
  string pans;
  for(int i = 1; i<cases + 1; i++){
    cin >> pans;
    int flips = 0;
    char prev, now;
    prev = pans[0];
    for(int j = 1; j<pans.size(); j++){
      now = pans[j];
      if(now != prev){
        flips++;
      }
      prev = now;
    }
    if(pans.size() == 1){
      now = pans[0];
    }
    if(now == '-'){
      flips++;
    }
    cout << "Case #" << i << ": " << flips << endl;
  }
}
