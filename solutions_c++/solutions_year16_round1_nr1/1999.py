#include <string>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
void win(string S){
    if(S.length()==1) {
        cout<<S<<endl;
        return;
    }
    string S1;
    char s0 = S[0];
    S1.push_back(S[0]);
    for(int i=1;i<S.length();i++)
        if(s0-S[i]>0)
            S1.push_back(S[i]);
        else
        {
            s0 = S[i];
            S1.insert(0,1,s0);
        }
    cout<<S1<<endl;    
    }
    
int main() {
  int t;
  string S;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> S;  // read n and then m.
    cout << "Case #" << i << ": " ;
    win(S);
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}


