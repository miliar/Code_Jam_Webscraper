#include <iostream>

using namespace std;

int main() {
	char s[200];
	int T;
	int t = 1;

	cin >> T;
	while (t <= T) {
		cin >> s;

		int count = 0;
		for (int i = 1; i < strlen(s); i++)
			if (s[i] != s[i-1])
				count++;

		if (s[strlen(s)-1] == '-')
			count++;

		cout << "Case #" << t << ": " << count << endl;

		t++;
	}
}