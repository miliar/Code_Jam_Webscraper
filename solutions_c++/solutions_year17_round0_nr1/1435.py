#include<iostream>

using namespace std;

int my_strlen(char* input) {
	int idx = 0;
	while (input[idx] != '\0')
		idx++;
	return idx;
}

int main() {
	int cnt;
	cin >> cnt;
	for (int itr = 0; itr < cnt; itr++)
	{
		char input[1001];
		int f;
		cin >> input >> f;
		int len = my_strlen(input);
		int num = 0;
		for (int i = 0; i < len-f+1; i++)
		{
			if (input[i] == '-') {
				for (int j = 0; j < f; j++)
				{
					if (input[i + j] == '-') {
						input[i + j] = '+'; 
					}
					else {
						input[i + j] = '-';
					}
				}
				num++;
			}
		}
		cout << "Case #" << itr + 1 << ": ";
		bool chk = true;
		for (int i = 1; i < f; i++)
		{
			if (input[len - i] == '-') {
				chk = false;
				break;
			}
		}
		if (chk)
			cout << num << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}