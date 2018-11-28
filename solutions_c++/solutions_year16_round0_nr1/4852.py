#include <iostream>
using namespace std;

int main() {
  int i, j, c, t, n;
  int val = (1<<10) - 1, ret = 0;
  cin >> t;
  c = 1;
  while (c <= t) {
    cin >> n;
    j = n;
    ret = 0;
    cout<<"Case #"<<c<<": ";
    if (n == 0) cout<<"INSOMNIA"<<endl;
    else {
      while (1) {
        i = j;
        while (i != 0){
          ret |= 1<<(i%10);
          i/=10;
        }
        if (ret == val) break;
        j += n;
      }
      cout<<j<<endl;
    }
    c++;
  }
  return 0;
}
