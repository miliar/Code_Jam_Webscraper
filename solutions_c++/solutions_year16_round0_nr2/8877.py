#include<iostream>
#include<string.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int _ = 0; _ < T; _++) {
		char stack[100];
		int count = 0;
		cin >> stack;
		if (stack[0] == '-')
			count = 1;
		for(int i = 1; i < strlen(stack); i++) {
			if (stack[i] == '-') {
				if (stack[i-1] != '-')
					count = count + 2;
			}
		}
		cout << "Case #" << _ + 1 << ": " << count << endl;
	}
	return 1;
}
