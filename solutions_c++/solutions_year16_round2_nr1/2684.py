#include<iostream>
using namespace std;

int main() {
	int cnt;
	cin >> cnt;
	for (int itr = 0; itr < cnt; itr++)
	{
		cout << "Case #" << itr + 1 << ": ";
		char* input = new char[2000];
		cin >> input;
		int* chk = new int[26];
		for (int i = 0; i < 26; i++)
		{
			chk[i] = 0;
		}
		int idx = 0;
		while (input[idx] != '\0') {
			chk[input[idx] - 'A']++;
			idx++;
		}
		int* result = new int[10];
		result[0] = chk[25];
		result[2] = chk[22];
		result[4] = chk[20];
		result[1] = chk[14] - result[0] - result[2] - result[4];
		result[3] = chk[17] - result[4] - result[0];
		result[5] = chk[5] - result[4];
		result[6] = chk[23];
		result[7] = chk[18] - result[6];
		result[8] = chk[7] - result[3];
		result[9] = (chk[13] - result[1] - result[7]) / 2;
		for (int i = 0; i < 10; i++)
		{
			while (result[i] != 0) {
				cout << i;
				result[i]--;
			}
		}
		cout << endl;
	}
	return 0;
}