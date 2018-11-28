#include <iostream>
#include <sstream>

using namespace std;

int main()
{                             
  ios::sync_with_stdio(false);
  int T;
  cin >> T;
  
  for(int t=1; t<=T; ++t) {
    string S;
    cin >>S;
    char buf[2005] = {0};
    int b=1000;
    int e=1001;
    buf[b]=S[0];
    for(size_t j=1; j<S.length(); ++j) {
      if(S[j] >= buf[b]) {
        b--;
        buf[b] = S[j];
      } else {
        buf[e++] = S[j];
      }
    }
    cout <<"Case #"<<t<<": "<<buf+b<<endl; 
  }                                       
}