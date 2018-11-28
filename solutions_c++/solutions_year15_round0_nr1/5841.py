#include <iostream>
using namespace std;

int main() {
	int n;
	cin >> n;

	for (int i=0;i<n;i++) {
		int count=0;
		std::string s;
		cin >> count >> s;
		int result = 0;
		int ob = 0;
		for (int j=0;j<=count;j++) {
			int c = s.at(j) - '0';
			if (ob < j) {
				result++;
				ob++;
			}
			ob+=c;
		}
		cout << "Case #" << i+1 << ": " << result << endl;
	}
	return 0;
}