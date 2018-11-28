#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <unordered_map>
#include <string>
#include <set>
#include <vector>
#include <cstring>
#include <algorithm>
#include <utility>
#include <iomanip>
#include <stack>
#include <string>

using namespace std;

string setup[10];
int order[10];

void init() {
	setup[0] = "ZERO"; setup[1] = "ONE"; setup[2] = "TWO"; setup[3] = "THREE";
	setup[4] = "FOUR"; setup[5] = "FIVE"; setup[6] = "SIX"; setup[7] = "SEVEN";
	setup[8] = "EIGHT"; setup[9] = "NINE";
	order[0] = 0;	order[1] = 2;	order[2] = 6;	order[3] = 7;
	order[4] = 5;	order[5] = 4;	order[6] = 8;	order[7] = 3;
	order[8] = 1;	order[9] = 9;
}


int main() {
	FILE * stream1, *stream2;
	freopen_s(&stream1, "Text.txt", "r", stdin);
	freopen_s(&stream2, "OUTPUT.txt", "w", stdout);
	int tcase,times;
	cin >> tcase;
	times = 1;
	init();
	while (tcase--) {
		string S;
		cin >> S;
		cout << "Case #" << times << ": ";
		int count[26];//count alphabet
		memset(count, 0, sizeof count);
		for (int i = 0; i < S.size(); i++) {
			count[(S[i] - 'A')] ++;
		}
		vector<int> ans;
		for (int j = 0; j < 10; j++) {
			string word = setup[order[j]];
			bool flag = true;
			for (int k = 0; k < word.size(); k++) 
				if (count[word[k] - 'A'] <= 0)
					flag = false;
			if (flag) {
				for (int k = 0; k < word.size(); k++)
					count[word[k] - 'A'] --;
				ans.push_back(order[j]);
				j--;
			}
		}
		sort(ans.begin(), ans.end());
		for (int i = 0; i < ans.size(); i++)
			cout << ans[i];
		cout << endl;
		times++;
	}
	return 0;
}