#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int rl;

bool check(bool *ar) {
	for (int i = 0; i < rl; i++) {
		if (*(ar + i) == false)
			return false;
	}
	return true;
}
int main() {
	int TestCase;
	FILE *fs, *fp;
	fs = fopen("input.txt", "r");
	fp = fopen("output.txt", "w");
	fscanf(fs, "%d", &TestCase);

	for (int iterTest = 0; iterTest < TestCase; iterTest++) {
		char arr[101] = { 0, };
		bool cake[101] = { 0, };
		int cnt = 0;
		int idx;
		fscanf(fs, "%s", arr);

		rl = strlen(arr);
		for (int i = 0; i < rl; i++) {
			if (arr[i] == '+')
				cake[i] = true;
		}
		while (check(cake) == false) {
			if (cake[0] == true) {
				idx = 0;
				while (cake[idx] == true&&idx<rl) {
					cake[idx] = !cake[idx];
					idx++;
				}
				std::reverse(cake, cake + idx);
			}
			else {
				idx = rl-1;
				while (cake[idx] == true&&idx>-1) {
					idx--;
				}
				for (int i = 0; i <= idx; i++)
					cake[i] = !cake[i];
				std::reverse(cake, cake + idx+1);
			}
			cnt++;
		}
		fprintf(fp, "Case #%d: %d\n", iterTest + 1,cnt);
	}
}