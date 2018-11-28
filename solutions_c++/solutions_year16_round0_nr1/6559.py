#include <iostream>
#include <fstream>

#define BUF 1024

using namespace std;

int canSleep(int N);
bool chkAnsSet(bool* ans, int size);

void main() {
	char* input = (char*)malloc(sizeof(char) * BUF);
	int t;
	int i;
	char* ans;
	ofstream outFile("output.txt");

	cin >> input;
	t = atoi(input);
	
	i = 1;
	ans = (char*)malloc(sizeof(char) * BUF);

	while (i <= t) {
		int n;
		int res;

		cin >> input;
		n = atoi(input);
		res = canSleep(n);
		if (res >= 0)
			sprintf(ans, "%d", res);
		else
			sprintf(ans, "INSOMNIA");

		printf("Case #%d: %s\n", i, ans);
		outFile << "Case #" << i << ": " << ans << endl;

		i++;
	}

	free(input);
	free(ans);
	outFile.close();
}
int canSleep(int n) {
	bool* anserSet = (bool*)malloc(sizeof(bool) * 10);
	int prev_name;
	int cur_name;
	int last_num;

	for (int i = 0; i < 10; i++)
		anserSet[i] = false;

	for (int i = 1;!chkAnsSet(anserSet, 10);i++) {
		prev_name = (i - 1) * n;
		cur_name = i * n;

		if (cur_name == prev_name) {
			last_num = -1;
			break;
		}

		int tmp = cur_name;
		last_num = cur_name;
		while (tmp > 0) {
			int one_digit = tmp % 10;
			tmp /= 10;
			anserSet[one_digit] = true;
		}

		prev_name = cur_name;
	}

	free(anserSet);
	return last_num;
}
bool chkAnsSet(bool* ansSet, int size) {
	for (int i = 0; i < size; i++)
		if (!ansSet[i])
			return false;
	return true;
}