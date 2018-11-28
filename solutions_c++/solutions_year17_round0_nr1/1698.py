#include <iostream>
#include <cstring>
using namespace std;

void flip(string& s, int start, int k){
	while (k > 0){
		if (s[start+k-1] == '+')
			s[start+k-1] = '-';
		else
			s[start+k-1] = '+';
		--k;
	}
}

int getResult(string& s, int k)
{
	if (k <= 0) return -1;
	int idx = 0, res = 0;
	while (idx+k <= s.size()){
		if (s[idx] == '-'){
			flip(s, idx, k);
			++res;
		}
		++idx;
	}
	for (int i = idx; i < s.size(); ++i)
		if (s[i] == '-') return -1;

	return res;
}

int main()
{
	int test = 0;
	cin >> test;
	string s;
	int k = 0;
	for (int t = 0; t < test; ++t){
		cin >> s >> k;
		int res = getResult(s, k);
		cout << "Case #" << t+1 << ": ";
		if (res == -1)
			cout << "IMPOSSIBLE\n";
		 else
			cout << res << endl;

	}

	return 0;
}
