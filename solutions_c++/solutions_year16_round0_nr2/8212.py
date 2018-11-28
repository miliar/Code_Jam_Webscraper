#include <iostream>

using namespace std;

int main()
{
	int t, i, count, a;
	char str[200];

	cin >> t;
	for (a = 0; a < t; ++a) {
		count = 0;
		cin >> str;
		for (i = 1; str[i] != '\0'; ++i) {
			if (str[i] != str[i-1]) {
				count++;
			}
		}
		if (str[i-1] == '-') {
			count++;
		}
		
		cout << "Case #" << a+1 << ": " << count << endl;
	}

	return 0;
}
