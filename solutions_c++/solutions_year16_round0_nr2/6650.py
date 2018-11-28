#include <iostream>
#include <fstream>

using namespace std;

#define BUF 1024

int getSol(char* in);
bool isAllHappy(bool* solset, int size);

void main() {
	char* input = (char*)malloc(sizeof(char) * BUF);
	int t;
	ofstream outFile("output.txt");

	cin >> input;
	t = atoi(input);

	for (int i = 1;i <= t;i++) {
		cin >> input;
		int sol = getSol(input);
		printf("Case #%d: %d\n", i, sol);
		outFile << "Case #" << i << ": " << sol << endl;
	}

	free(input);
	outFile.close();
}
int getSol(char* in) {
	int str_len = strlen(in);
	bool* stk_cake = (bool*)malloc(sizeof(bool) * str_len);
	int cnt = 0;

	//initialize
	for (int i = 0; i < str_len; i++)
		if (in[i] == '+')
			stk_cake[i] = true;
		else
			stk_cake[i] = false;
	//initialize

	while (!isAllHappy(stk_cake, str_len)) {
		cnt++;
		bool start = stk_cake[0];

		//reverse
		for (int i = 0;stk_cake[i] == start && i < str_len; i++) {
			stk_cake[i] = !stk_cake[i];
		}
	}

	free(stk_cake);
	return cnt;
}
bool isAllHappy(bool* solset, int size) {
	for (int i = 0; i < size; i++)
		if (!solset[i])
			return false;
	return true;
}