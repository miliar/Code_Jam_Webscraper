#include <iostream>

using namespace std;
typedef long long ll;

void process(ll A, ll B, ll K)
{
  ll count = 0L;
  for(ll i=0L; i<A; ++i) {
    for(ll j=0L; j<B; ++j) {
      if((i&j) < K) {
	count++;
      }
    }
  }
  cout << count;
}


int main(int argc, char** argv)
{
  int T;
  long long A, B, K;

  cin >> T;
  for(int i=1; i<=T; i++) {

    cin >> A >> B >> K;
    cout << "Case #" << i << ": ";
    // cout << A << B << K << endl;

    process(A, B, K);

    cout << endl;
  }

  return 0;
}
