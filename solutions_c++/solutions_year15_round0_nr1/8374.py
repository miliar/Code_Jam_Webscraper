#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for ( int t=1; t<=T; ++t ) {
    int N;
    string a;
    cin >> N >> a;

    vector<int> b;
    b.reserve(N+1);
    b[0] = static_cast<int>(a[0]-'0');
    for ( int i=1; i<=N; ++i ) {
      b[i] = b[i-1] + static_cast<int>(a[i]-'0');
    }

    int ans = 0;
    for ( int i=1; i<=N; ++i ) {
      if ( b[i-1] < i ) {
        int additional = i - b[i-1];
        ans = max(ans, additional);
      }
    }

    cout << "Case #" << t << ": " << ans << endl;
  }
}
