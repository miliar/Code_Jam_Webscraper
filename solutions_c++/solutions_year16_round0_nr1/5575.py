#include <iostream>
#include <vector>
using namespace std;
#include <cstdio>

typedef long long int ll;

void upd(ll t, vector<int> &num){
  while(t){
    num[t%10] = 1;
    t /= 10;
  }
}

int main(void){
  int t;
  cin >> t;
  for(int ll = 0; ll < t; ll++){
    long long int ans = 0LL;
    int n;
    cin >> n;
    vector<int> num(10, 0);
    for(int nn = 1; nn < 2000; nn++){
      long long int x = nn * n;
      upd(x, num);
      int f = 1;
      for(int i = 0; i < 10; i++){
        if(!num[i]) f = 0;
      }
      if(f){
        ans = x;
        break;
      }
    }
    if(ans) cout << "Case #" << ll + 1 << ": " << ans << endl;
    else cout << "Case #" << ll + 1 << ": " << "INSOMNIA" << endl;
  }
}
