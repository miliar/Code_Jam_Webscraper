#include <iostream>
#include <string>

using namespace std;

int main() {
	int T, n;
	int counter, a, maxa;
	string tmp;
	cin >> T;
	for (int i=0; i!=T; i++) {
		maxa = 0;
		counter = a = 0;
		
		cin >> n >> tmp;
		
		for (int j=0; j <= n; j++) {
			a = 0;
			if (counter < j) a += j - counter;
			counter += a + tmp[j]-'0';
			maxa += a;
		}
		
		cout << "Case #" << i+1 << ": " << maxa << '\n';
	}	
	return 0;
}