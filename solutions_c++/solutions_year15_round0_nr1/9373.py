#include <iostream>
#include <string>
#define rep(i, a, b) for(int i=int(a); i<int(b); i++)

using namespace std;

int main() {
	int T;
	cin >> T;
	rep(t, 0, T) { 
		int smax = 0;
		cin >> smax;

		string str;
		cin >> str;

		int count = 0;
		int toadd = 0;
		rep(i, 0, smax+1) {
			if(str[i]-'0' > 0 && count < i) {
				toadd += i-count;
				count = i;
			}
			count += str[i]-'0';
		}

		cout << "Case #" << (t+1) << ": " << toadd << endl;
	}
	return 0;
}
