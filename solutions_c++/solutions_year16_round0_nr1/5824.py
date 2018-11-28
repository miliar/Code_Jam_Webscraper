#include <iostream>
#include <string>

using namespace std;


int main(void)
{
	int d;
	cin >> d;
	for (int i = 1; i <= d; i++) {
		int n;
		cin >> n;

		int count = 0;
		int ok[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

		if (n == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		while(1) {
			count++;
			string s;
			s = to_string(count * n);	
			char a = '0';
			for (int j = 0; j < s.length(); j++) ok[(int)s[j] - a] = 1;
			int finish = 0;
			for (int j = 0; j < 10; j++) {
				if (ok[j] == 0) break;
				if (j == 9) finish = 1;
			}
			if (finish) break;
		}

		cout << "Case #" << i << ": " << count * n << endl;
	}
	return 0;
}
