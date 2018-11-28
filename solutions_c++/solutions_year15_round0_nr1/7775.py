#include <iostream>
#include <cstdlib>

using namespace std;

void test(int t) {

	int s, result = 0, up = 0;
	string in;
	
	cin >> s;
	getline(cin, in);
	
	for (int i=1; i<in.length(); ++i) {
		if (up < i-1) {
			result += i-1-up;
			up = i-1;
		}
		up += in[i]-'0';
	}
	
	cout << "Case #" << t << ": " << result << endl;
}

int main() {
	
	int t;
	cin >> t;
	for (int i=1; i<=t; ++i)
		test(i);
		
	return 0;
}
