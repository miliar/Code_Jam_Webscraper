#include <iostream>
#include <string>

using namespace std;

#define ll long long int
#define endl '\n'

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for (int Case = 1; Case <= T; Case++){
		string S;
		cin >> S;
		string ret = S.substr(0, 1);
		for (int i = 1; i < S.size(); i++){
			string cur = S.substr(i, 1);
			string first = ret.substr(0, 1);
			if (cur >= first) ret = cur + ret;
			else ret += cur;

		}

		cout << "Case #" << Case << ": " << ret << endl;
	}
}