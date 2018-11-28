#include <iostream>
#include <string>
using namespace std;

int solve(int smax, string& s){
	int curr = 0, ans = 0;
	for (int i=0; i<=smax; ++i) {
		if (i > curr) {
			ans += (i - curr);
			curr = i;
		}
		int n = s[i] - '0';
		curr += n;
	}
	return ans;
}
int main()
{
  int _T; cin >> _T; // 1-100
  for (int _t=1; _t<=_T; ++_t) {
  	int Smax; cin >> Smax;
  	string s; cin >> s;

 answer:
    cout << "Case #" << _t << ": " << solve(Smax,s) << endl;
  }
}
