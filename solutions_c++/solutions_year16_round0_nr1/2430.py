#include <bits/stdc++.h>
using namespace std;

int t, n, d[10];

int main(){
  cin >> t;
  int cnt=0;
  while (t--){
    cnt++;
    cin >> n;
    if (n==0) cout << "Case #" << cnt << ": INSOMNIA\n"; else{

        memset(d, 0, sizeof d);
        int p=0, x;
        for (int j=0; j<=200; j++) {
           p+=n;
           x=p;
           while (x){
             d[x%10]++;
             x/=10;
           }
           bool fake=true;
           for (int k=0; k<=9; k++) if (d[k]==0) fake=false;
           if (fake) break;

        }
        cout << "Case #" << cnt << ": " << p << endl;
      }
  }


}
