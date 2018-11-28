#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int a0 = 1; a0 <= t; a0++){
        int k;
        int c,s;
        cin >> k >> c >> s;
        cout<<"Case #"<<a0<<":";
      for(int i=1;i<=s;i++){
          cout<<" "<<i;
      }
        cout<<"\n";
    }
    return 0;
}