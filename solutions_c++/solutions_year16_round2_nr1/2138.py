#include<stdio.h>
#include<vector>
#include<string>
#include<algorithm>
using std::pair;
using std::string;

int cnt[26] = { 0, };
std::vector<pair<int,int>> ans;
void check(int num, string numstr, char key) {
	bool flag = false;

	int p = cnt[key - 'A'];
	int temp[26] = { 0, };
	for (int i = 0; i < 26; i++) {
		temp[i] = cnt[i];
	}

	for (char ch : numstr) {
		temp[ch - 'A'] -= p;
	}
	for (int i = 0; i < 26; i++) {
		if (temp[i] < 0) {
			flag = true;
			break;
		}
	}
	if (!flag) {

		ans.push_back({ num,p });
		for (char ch : numstr) {
			cnt[ch - 'A'] -= p;
		}
	}
}



int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for (int t = 1; t <= tc; t++) {
		ans.clear();
		for (int i = 0; i < 26; i++) {
			cnt[i] = 0;
		}
		char str[2010];
		scanf("%s", str);
		for (int i = 0; str[i] != '\0'; i++) {
			cnt[str[i] - 'A']++;
		}
		check(6, "SIX", 'X');
		check(7, "SEVEN", 'S');
		check(5, "FIVE", 'V');
		check(8, "EIGHT", 'G');
		check(4, "FOUR", 'F');
		check(9, "NINE", 'I');
		check(3, "THREE", 'H');
		check(2, "TWO", 'W');
		check(1, "ONE", 'N');
		check(0, "ZERO", 'Z');
		std::sort(ans.begin(),ans.end());
		printf("Case #%d: ", t);
		for (auto a : ans) {
			for (int i = 0; i < a.second; i++) {
				printf("%d", a.first);
			}
		}
		printf("\n");
	}
}