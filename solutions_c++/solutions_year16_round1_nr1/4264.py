#include<iostream>
using namespace std;

void lastword(char * s) {
	char buffer[1024];
	char result[1024];

	buffer[0] = s[0];
	buffer[1] = '\0';
	for (int i = 1; i < strlen(s); i++) {
		if (s[i] < buffer[0]) {
			snprintf(result, i + 2, "%s%c", buffer, s[i]);
		}
		else {
			snprintf(result, i + 2, "%c%s", s[i], buffer);
		}
		snprintf(buffer, strlen(result) + 1, "%s", result);
	}
	cout << buffer;
}

int main() {
	int T;
	char buffer[128][1024];

	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> buffer[t];
	}

	for (int t = 0; t < T; t++) {
		cout << "Case #" << t + 1 << ": ";
		lastword(buffer[t]);
		cout << endl;
	}

	//system("pause");
	return 0;
}