#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <set>
using namespace std;

set<__int128> primes;

__int128 conv(const string& x, int base) {
  int l = x.size();
  __int128 t = 1;
  __int128 s = 0;
  for(int i=0;i<l;++i) {
    s += (x[l-i-1]-'0')*t;
    t *= base;
  }
  return s;
}

void gen(int N, int count) {
  __int128 max_num = ((__int128)1)<<(N-2);

  for(__int128 n=0;n<max_num;++n)
  {
    string x = "1";
    __int128 t = n;
    for(__int128 d=2;d<N;++d)
    {
      if(t>0) {
        if(t%2==0) x+="0";
        else x += "1";
        t/=2;        
      } else {
        x += "0";
      }
    }

    x += "1";

    bool valid = true;    

    vector<__int128> fs;
    

    for(int b=2;b<=10;++b) {
      __int128 rep = conv(x, b);      
      for(__int128 i=2;i<=min(100000.0, sqrt(rep));++i)
        if(rep % i==0) {
          fs.push_back(i);
          break;
        }
    }

    if(!(fs.size()==9)) continue;

    cout<<x;

    for(auto f: fs)
      cout<<" "<<(long long)f;

    cout<<endl;

    if(--count==0) break;
  }
}

int main() {  
  int N, J;
  cin>>N>>J; 
  cout<<"Case #1:"<<endl;
  gen(N, J);  
  return 0;
}