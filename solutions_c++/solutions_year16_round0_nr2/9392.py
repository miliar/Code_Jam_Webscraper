#include <iostream>
#include <vector>
using namespace std;


int main(){
  int cases;
  string cur;
  cin >> cases;

  for(int i = 0; i < cases; i++){
    cin >> cur;
    int flips = 0;
    char last = '$';
    for(char c: cur){
      if(last == '$'){last = c;}
      if(c != last){flips++;}
      last = c;
    }
    if(cur[cur.length() - 1] == '-') {flips++;}
    cout << "Case #" << i+1 << ": "  << flips << endl;
  }
  return 0;
}
