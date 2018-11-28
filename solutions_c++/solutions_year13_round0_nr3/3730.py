#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

char *buf = new char[100];

bool pal(ll x) {
  string s = itoa(x,buf,10);
  int n=s.size();
  for(int i=0;i<n/2;i++){
    if(s[i]!=s[n-i-1]){
      return false;
    }
  }
  return true;
}

int main(){
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);
  int Q;
  cin >> Q;
  for(int q=0;q<Q;q++) {
    cout << "Case #" << q+1 << ": ";
    ll a,b;
    cin >> a >> b;
    ll aa = max(sqrt(a+0.)-10, 1.);
    ll bb = sqrt(b+0.)+10;
    ll k = 0;
    for(ll i=aa;i<=bb;i++){
      if (pal(i) && pal(i*i) && i*i>=a && i*i<=b){
        k++;
      }
    }
    cout << k << endl;
  }
  return 0;
}