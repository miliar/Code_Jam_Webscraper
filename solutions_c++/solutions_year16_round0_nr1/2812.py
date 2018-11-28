#include <iostream>
#include <set>
#include <unordered_set>
using namespace std;

void append(set<int>& d, int n) {
  while(n>0) {
    d.insert(n%10);
    n/=10;
  }
}

int main() {
  int t, N, n;
  cin>>t;
  for(int c=1;c<=t;++c)
  {
    cin>>N;

    int ans = -1;
    

    set<int> d;
    unordered_set<int> f;

    n = N;

    while(true) {
      if(f.count(n)) break;
      f.insert(n);
      append(d, n);
      if(d.size()==10) {        
        ans = n;
        break;
      }
      n += N;
    }

    cout<<"Case #"<<c<<": ";
    if(ans == -1)
      cout<<"INSOMNIA"<<endl;
    else
      cout<<ans<<endl;
  }
  return  0;
}