#include <cstdio>
#include <iostream>

using namespace std;

void change(char[], int idx);
int main()
{
	int T;
	char str[1001];

	cin >> T;
	for (int j = 1; j <= T; j++) {
		cin >> str;

		for (int i = 1; str[i] != 0; i++) {
			if (str[i] >= str[0]) change(str, i);
		}

		printf("Case #%d: %s\n", j, str);
	}

	return 0;
}
void change(char s[], int idx)
{
	char tmp = s[idx];

	for (int i = idx; i > 0; i--) {
		s[i] = s[i - 1];
	}

	s[0] = tmp;
}