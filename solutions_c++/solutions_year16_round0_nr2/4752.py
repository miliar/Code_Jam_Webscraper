#include <iostream>
#include <string>
using namespace std;

string S;

int main()
{
  int T;
  cin >> T;
  getline(cin, S);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    getline(cin, S);
    int N = S.length();
    
    // count
    int swaps = 0;
    for (int n = N - 1; n >= 0; --n)
      if ((swaps % 2 == 0 && S[n] == '-') or (swaps % 2 == 1 && S[n] == '+'))
	swaps++;
    
    // output
    cout << "Case #" << Ti << ": " << swaps << endl;
  }
  return 0;
}
