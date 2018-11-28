#include <iostream>
#include <string>
using namespace std;

int main() {
	int T, t, N, i, tmp, RES;
	string n;
	
	cin >> T;
	for (t=1; t<=T; t++) {
		cin >> N >> n;
		
		tmp = RES = 0;
		for (i=0; i<=N; i++) {
			if (RES+tmp < i) RES += i - (RES+tmp);
			tmp += n[i]-'0';
		}
		cout << "Case #" << t << ": " << RES << endl;
	}

	return 0;
}
