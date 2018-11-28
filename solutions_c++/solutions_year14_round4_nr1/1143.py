#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
#include <iostream>

using namespace std;

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  cin >> T;
  for(int t=0; t<T;t++){
    int n,x;
    cin >> n >> x;
    vector<int> a(n);
    for (int i = 0; i<n;i++){
      cin >> a[i];
    }
    sort(a.begin(),a.end());
    int s = 0;
    int i = 0;
    for (int j = n-1; j>=i;j--){
      s += 1;
      if (a[j] + a[i] <= x)
        i += 1;
    }
    cout << "Case #" << t+1 << ": " << s << endl;
  }
  return 0;
}
