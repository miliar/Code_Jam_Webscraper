#include<bits/stdc++.h>
using namespace std;
typedef long long int64;

struct TheLastWord
{
  TheLastWord()
  {
    string S;
    cin >> S;
    string ret = "";
    for(int i = 0; i < S.size(); i++) {
      ret = max(ret + S[i], S[i] + ret);
    }
    cout << ret << endl;
  }
};


int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    new TheLastWord();
  }
  return(0);
}
