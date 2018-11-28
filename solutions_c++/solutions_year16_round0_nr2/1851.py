#include <string>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int CountDiff(string k){
    k.push_back('+');
    int len = k.length();
    int count=0;
    for(int i = len-1;i>0;i--){
        if(k[i]!=k[i-1])
        count++;
    }
    return count;
}

int main() {
  int t;
  string k;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> k;  // read n and then m.
    cout << "Case #" << i << ": " << CountDiff(k) << " " << endl;
  }
  return 0;
}
