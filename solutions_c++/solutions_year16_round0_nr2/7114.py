#include <iostream>
#include <string>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("Ans.txt", "w", stdout);
	int t; scanf("%d", &t);
	int Case = 0;
	while (t--) {
		int count = 0, plus = 0;
		string str;
		cin >> str;
		while (1) {
			int ch = -1;
			for (int i = 0; i < str.size() - 1; i++) {
				if (str[i] != str[i + 1] && str.size() != 1) {
					ch = i;
					break;
				}
				else if (str[i] == '+') {
					plus++;
				}
			}
			if (str[str.size() - 1] == '+')
				plus++;
			if (plus == 0 && ch == -1)
				ch = str.size() - 1;

			
			if (plus == str.size()) {
				printf("Case #%d: %d\n", ++Case, count);
				break;
			}
			count++;
			for (int i = 0; i <= ch; i++) {
				if (str[i] == '+')
					str[i] = '-';
				else
					str[i] = '+';
			}
			plus = 0;
		}
	}
}