#include<iostream>
#include<string>
#include<algorithm>

void calc(int test_num) {
	std::string s;

	std::cin >> s;

	int alpha_num[26] = { 0 };
	char alpha[] = { "ABCDEFGHIJKLMNOPQRSTUVWXYZ" };

	for (int i = 0; i < 26; i++) {
		alpha_num[i] = std::count(s.begin(), s.end(), alpha[i]);
	}

	std::string ans = "";

	// 6 x
	while (alpha_num[23] > 0) {
		ans += '6';
		alpha_num[23]--; // x
		alpha_num[18]--; // s
		alpha_num[8]--; // i
	}

	// 8 g
	while (alpha_num[6] > 0) {
		ans += '8';
		alpha_num[4]--;
		alpha_num[8]--;
		alpha_num[6]--;
		alpha_num[7]--;
		alpha_num[19]--;
	}

	// 4 u
	while (alpha_num[20] > 0) {
		ans += '4';
		alpha_num[5]--;
		alpha_num[14]--;
		alpha_num[20]--;
		alpha_num[17]--;
	}

	// 0 z
	while (alpha_num[25] > 0) {
		ans += '0';
		alpha_num[25]--;
		alpha_num[4]--;
		alpha_num[17]--;
		alpha_num[14]--;
	}

	//2 w
	while (alpha_num[22] > 0) {
		ans += '2';
		alpha_num[19]--;
		alpha_num[22]--;
		alpha_num[14]--;
	}

	// 3 r
	while (alpha_num[17] > 0) {
		ans += '3';
		alpha_num[19]--;
		alpha_num[7]--;
		alpha_num[17]--;
		alpha_num[4] -= 2;
	}

	// 7 s
	while (alpha_num[18] > 0) {
		ans += '7';
		alpha_num[18]--;
		alpha_num[4] -= 2;
		alpha_num[21]--;
		alpha_num[13]--;
	}

	// 1 o
	while (alpha_num[14] > 0) {
		ans += '1';
		alpha_num[14]--;
		alpha_num[13]--;
		alpha_num[4]--;
	}



	// 5
	while (alpha_num[5] > 0) {
		ans += '5';
		alpha_num[5]--;
		alpha_num[8]--;
		alpha_num[21]--;
		alpha_num[4]--;
	}

	// 9
	while (alpha_num[8] > 0) {
		ans += '9';
		alpha_num[13] -= 2;
		alpha_num[8]--;
		alpha_num[4]--;
	}

	std::sort(ans.begin(), ans.end());

	std::cout << "Case #" << test_num << ": " << ans << std::endl;
}



int main() {
	int test_case;

	std::cin >> test_case;

	for (int i = 0; i < test_case; i++) {
		calc(i + 1);
	}

	return 0;
}