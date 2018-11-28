#include <iostream>
using namespace std;

int
main() {
  int T;
  cin>>T;
  for(int i=1;i<=T;i++) {
    int S,
        standing=0,
        friends=0;
    char c;
    cin>>S;
    for(int x=0; x<=S; x++) {
      cin>>c;
      int temp = c - '0';
      if ( standing < x ) {
        friends += x - standing;
        standing += x - standing;
      }
      standing += temp;
    }
    cout<<"Case #"<<i<<": "<<friends<<'\n';
  }
}
