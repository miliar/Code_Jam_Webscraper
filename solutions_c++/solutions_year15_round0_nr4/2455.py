#include <iostream>
using namespace std;
int main() {
	int tc;
	cin>>tc;
	int count = 1;
	while (tc--) {
		int x, r, c;
		cin>>x>>r>>c;
		if (r > c) r ^= c ^= r ^= c;
		bool win = false;
		if (x == 1) win = true;
		else if (x == 2) {
			if ((r*c) % x == 0) win = true;
			else win = false;
		} else if (x == 3) {
			if (r == 1 || c <= 2) win = false;
			else if (r == 2 && c == 3) win = true;
			else if (r == 2 && c == 4) win = false;
			else if (r == 3 && c == 3) win = true;
			else if (r == 3 && c == 4) win = true;
			else if (r == 4 && c == 4) win = false;
		} else {
			if ((r == 3 && c == 4) || (r == 4 && c == 4)) win = true;
			else win = false;
		}
		
		cout<<"Case #"<<count++<<": ";
		if (win)
			cout<<"GABRIEL"<<endl;
		else 
			cout<<"RICHARD"<<endl;
	}
	return 0;
}
