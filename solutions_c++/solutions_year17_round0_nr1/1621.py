#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void flip(char& c) {
	if (c == '-') c = '+';
	else c = '-';
}

int main() {

	std::ifstream in("C:/Users/Yoav/Jam/Qual/A-large.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("c:/Users/Yoav/Jam/Qual/out.txt");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		int k;
		cin >> s >> k;
		int i = 0, n = s.length(), cnt = 0;
		for (; i <= n - k; i++) {
			if (s[i] == '-') {
				cnt++;
				for (int j = i; j < i + k; j++)
					flip(s[j]);
			}
		}
		bool ans = true;
		for (; i < n; i++) 
			if (s[i] == '-') {
				ans = false;
				break;
			}
		cout << "Case #" << t << ": ";
		if (ans)	cout << cnt << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

	// your code goes here
	return 0;
}
