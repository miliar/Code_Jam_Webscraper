#include <iostream>
#include <cstdlib>

using namespace std;

long long NSD(long long a, long long b) {
  while (a!=b)
    if (a<b) b-=a;
    else a-=b;
  return a;
}

int main() {

int T;

cin >> T;
for (int i=1; i<=T; i++) {
  int r;
  string l;
  long long p,q,n;
  cin >> l;
  p=atol(l.c_str());
  r=l.find('/');
  q=atol(l.c_str()+r+1);
  r=0;

  if (p>0) {
    n=NSD(p,q);
    if (n>1) {p/=n;q/=n;}
    while (p<q) {p*=2; r++;}
    while ((q>1) && ((q&1)==0)) q/=2;
  }  
  cout << "Case #" << i << ": ";
  if ((r==0) || (q>1))
    cout << "impossible";
  else
    cout << r;
  cout << '\n';
  }
}
