#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

#define For(i,a,b)  for(int i=(a);i<(b);++i)
#define rep(i,n)    For(i,0,(n))

string solve()
{
	string S;
	int K;

	cin >> S >> K;

	int result = 0;
	rep(i, S.size() - K + 1) {
		if(S[i] == '-') {
			++result;
			rep(j, K) {
				if(S[i+j] == '-') {
					S[i+j] = '+';
				} else {
					S[i+j] = '-';
				}
			}
		}
	}
	if(find(S.begin(), S.end(), '-') == S.end())
		return to_string(result);
	else
		return "IMPOSSIBLE";
}

int main()
{
	int T;
	cin >> T;

	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
}
