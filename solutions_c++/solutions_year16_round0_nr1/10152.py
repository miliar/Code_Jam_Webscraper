#include <bits/stdc++.h>

using namespace std;

long solver (int x){
    set<int> numset;
    int xx, chc, cp, i=1;
    while(numset.size()<10){
      xx = x * i;
      cp = xx;
        while(xx > 0){
        chc = xx%10;
        xx /= 10;
        numset.insert(chc);
      }
      i++;
    }
    return cp;
}

int main(){
  int t, x;
  int i=1;
  cin >> t;
  while(t--){
      long ans;
      cin >> x;
      if (x == 0){
        cout << "Case #" << i << ": " "INSOMNIA" << endl;
        i++;
      }else{
        ans = solver(x);
        cout << "Case #" << i << ": " << ans << endl;
        i++;
      }
  }
return 0;
}
