#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> ans;

bool isExist(int num, string &str, int len) {
	string num_str;

	switch (num) {
		case 0:
			num_str = "ZERO";
			break;
		case 1:
			num_str = "ONE";
			break;
		case 2:
			num_str = "TWO";
			break;
		case 3:
			num_str = "THREE";
			break;
		case 4:
			num_str = "FOUR";
			break;
		case 5:
			num_str = "FIVE";
			break;
		case 6:
			num_str = "SIX";
			break;
		case 7:
			num_str = "SEVEN";
			break;
		case 8:
			num_str = "EIGHT";
			break;
		case 9:
			num_str = "NINE";
			break;
	}

	int nlen = num_str.size();	
	bool cond = true;

	for (int i = 0; i < nlen; i++) {
		bool flag = false;
		for (int j = 0; j < len; j++) {
			if (num_str[i] == str[j]) {			
				flag = true;
				break;
			}				
		}
		if (!flag) {
			cond = false;
			break;
		}		
	}
	if (cond) {
		//지우는 역할
		return true;
	}
	else
		return false;
}

bool isFinish(string str,int len) {
	for (int i = 0; i < len; i++) {
		if (str[i] != 'x')
			return false;
	}
	return true;
}
void del(string &str, int len, int num) {
	string num_str;

	switch (num) {
	case 0:
		num_str = "ZERO";
		break;
	case 1:
		num_str = "ONE";
		break;
	case 2:
		num_str = "TWO";
		break;
	case 3:
		num_str = "THREE";
		break;
	case 4:
		num_str = "FOUR";
		break;
	case 5:
		num_str = "FIVE";
		break;
	case 6:
		num_str = "SIX";
		break;
	case 7:
		num_str = "SEVEN";
		break;
	case 8:
		num_str = "EIGHT";
		break;
	case 9:
		num_str = "NINE";
		break;
	}
	int nlen = num_str.size();
	for (int i = 0; i < nlen; i++) {
		for (int j = 0; j < len; j++) {
			if (num_str[i] == str[j]) {
				str[j] = 'x';
				break;
			}
		}
	}

}

void dfs(int num, string str, int len) {
	if (num > 9)
		return;
	if (isFinish(str, len)) {
		sort(ans.begin(), ans.end());

		for (int i = 0; i < ans.size(); i++)
			printf("%d", ans[i]);
		return;
	}

	if (isExist(num, str, len)) {
		dfs(num + 1, str, len);

		ans.push_back(num);
		del(str, len, num);
		dfs(num, str, len);
		ans.pop_back();
	}
	else {
		dfs(num + 1, str, len);
	}
}
void solve() {
	ans.clear();
	string str;
	cin >> str;
	int len = str.size();	

	dfs(0, str, len);
	
}

int main(void) {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ",i+1);
		solve();
		printf("\n");
	}

}