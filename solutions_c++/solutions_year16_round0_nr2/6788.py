#include<iostream>
using namespace std;

int main() {
	int cnt;
	cin >> cnt;
	for (int itr = 0; itr < cnt; itr++)
	{
		char* input = new char[100];
		cin >> input;
		char chk = input[0];
		int result = 0;
		for (int i = 0; i < strlen(input); i++)
		{
			if (chk != input[i]) {
				result++;
				chk = input[i];
			}
		}
		if (chk == '-') {
			result++;
		}
		cout << "Case #" << itr + 1 << ": ";
		cout << result << endl;
	}
	return 0;
}