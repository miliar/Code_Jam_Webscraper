#include <iostream>

using namespace std;

string s;
int n;
int tests;
int sum, ans;

int main(){
  cin >> tests;
  for(int cur_test = 1; cur_test <= tests; cur_test++)
  {
    sum = ans = 0;
    cin >> n >> s;
    for(int i = 0; i <= n; i++)
    {
      if(sum < i) {
        ans += (i - sum);
        sum = i;
      }
      sum += (s[i] - '0');
    }
    cout << "Case #" << cur_test << ": " << ans << "\n";
  }
  return 0;
}
