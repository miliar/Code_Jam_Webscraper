#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <iostream>

using namespace std;

bool check(vector<int> &a) {
  bool down = false;
  int n = a.size();
  for (int i = 1; i<n;i++){
    if (a[i-1] < a[i] && down){
      return false;
    }
    if (a[i-1] > a[i] && !down){
      down = true;
    }
  }
  return true;
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  cin >> T;
  for(int t=0; t<T;t++){
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i<n;i++){
      cin >> a[i];
    }
    vector<int> b(a);
    sort(b.begin(),b.end());
    int ans = 10000000;
    vector<int> res;
    do{
      if (!check(b)) {
        continue;
      }
      int s = 0;
      vector<int> c(a);
      for (int i = 0; i<n; i++){
        int x = find(c.begin(), c.end(), b[i]) - c.begin();
        while (x != i) {
          s+= 1;
          if (x > i) {
            swap(c[x], c[x-1]);
            x = x-1;
          }
          else{
            swap(c[x], c[x+1]);
            x = x + 1;
          }
        }
      }
      if (s < ans){
        ans = s;
        res = b;
      }
    }while (next_permutation(b.begin(), b.end()));
    cout << "Case #" << t+1 << ": " << ans << endl;
    /*for (int i =0;i<n;i++){
      cout << res[i] << " ";
    }
    cout << endl;*/
  }
  return 0;
}
