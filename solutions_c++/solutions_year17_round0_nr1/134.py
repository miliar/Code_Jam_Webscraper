#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int tc=1;tc<=T;++tc) {
		string S;
		int K, flips=0;
		cin >> S >> K;
		for (int i=0;i<=S.length()-K;++i) {
			if (S[i]=='-') {
				flips++;
				for (int j=0;j<K;++j) S[i+j]=(S[i+j]=='+'?'-':'+');
			}
		}
		bool impossible = false;
		for (int i=0;i<S.length();++i) if (S[i]=='-') impossible = true;
		cout << "Case #" << tc << ": ";
		if (impossible) cout << "IMPOSSIBLE\n";
		else cout << flips << endl;
	}
	return 0;
}