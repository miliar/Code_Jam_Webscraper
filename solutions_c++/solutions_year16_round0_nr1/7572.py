#include <bits/stdc++.h>

using namespace std;

int main(){
  freopen("A-large.in", "r", stdin);
  freopen("small_output.txt", "w", stdout);
   int t, N, n, Ans;
   cin >> t;
   for (int i = 0; i < t; i++) {
    cin >> n;
    cout << "Case #" << i + 1  << ": ";
    if (n == 0) {
        cout << "INSOMNIA";
        cout << endl;
    } else {int cnt =  0;
      vector<int> pod(10, 0);
      for (int j = 1; j <= 1000; j++) {
        N = n * j;
        Ans = N;
        while(N) {
            if (pod[N % 10] == 0) {
                pod[N % 10] = 1;
                cnt++;
            }
             N /= 10;
        }
        if (cnt == 10) {
            cout << Ans;
            break;
        }
      }
       cout << endl;
    }
   }







  return 0;
}
