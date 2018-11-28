#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

typedef long long ll;

ll strToNum(string S) {
	istringstream iss(S);
	ll n;
	iss >> n;
	return n;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		string C, J;
		cin >> C >> J;
		int N = C.size();
		while (C.size() < 3) {
			C = '0' + C;
			J = '0' + J; 
		}
		vector<string> Cs, Js;
		for (int i = (C[0] == '?' ? '0' : C[0]); i <= (C[0] == '?' ? '9' : C[0]); ++i) {
			for (int j = (C[1] == '?' ? '0' : C[1]); j <= (C[1] == '?' ? '9' : C[1]); ++j) {
				for (int k = (C[2] == '?' ? '0' : C[2]); k <= (C[2] == '?' ? '9' : C[2]); ++k) {
					string X = "";
					X += i;
					X += j;
					X += k;
					Cs.push_back(X);
				}		
			}
		}
		for (int i = (J[0] == '?' ? '0' : J[0]); i <= (J[0] == '?' ? '9' : J[0]); ++i) {
			for (int j = (J[1] == '?' ? '0' : J[1]); j <= (J[1] == '?' ? '9' : J[1]); ++j) {
				for (int k = (J[2] == '?' ? '0' : J[2]); k <= (J[2] == '?' ? '9' : J[2]); ++k) {
					string X = "";
					X += i;
					X += j;
					X += k;
					Js.push_back(X);
				}		
			}
		}
		string A = "999", B = "999";
		ll dif = 10000;
		for (int i = 0; i < Cs.size(); ++i) {
			for (int j = 0; j < Js.size(); ++j) {
				ll x = abs(strToNum(Cs[i]) - strToNum(Js[j]));
				if (x < dif) {
					dif = x;
					A = Cs[i];
					B = Js[j];
				} else if (x == dif) {
					dif = x;
					if (Cs[i] < A || Js[j] < B) {
						A = Cs[i];
						B = Js[j];
					}
				}
			}
		}
		cout << "Case #" << t << ": " << A.substr(3 - N, N) << " " << B.substr(3 - N, N) << "\n";
	}
	return 0;
}