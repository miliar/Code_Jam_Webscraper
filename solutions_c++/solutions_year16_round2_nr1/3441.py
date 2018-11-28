#include <stdio.h>
#include <string>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

string digit[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int num[26];
int flag;
int number[100];
string ans;

void dfs(int dep, int numb, int tot) {
	if (flag == true) {
		return;
	}
	if (tot == 0) {
		flag = true;
		int temp[100];
		for (int i = 0; i < dep; i++) {
			temp[i] = number[i];
		}
		sort(temp, temp+dep);
		ans = "";
		for (int i = 0; i < dep; i++) {
			ans = ans + char(temp[i] + '0');
		}
		return;
	}
	int temp = 1;
	for (int i = 0; i < digit[numb].size(); i++) {
		if (num[digit[numb][i] - 'A'] <= 0) {
			temp = 0;
		}
		num[digit[numb][i] - 'A']--;
	}
	if (temp == 0){
		for (int i = 0; i < digit[numb].size(); i++) {
			num[digit[numb][i] - 'A'] ++;
		}
		return;
	}
	number[dep] = numb;

	for (int i = 0; i < digit[numb].size(); i++) {
		// num[digit[numb][i] - 'A'] --;
		tot--;
	}
	for (int i = 0; i < 10; i++) {
		dfs(dep + 1, i, tot);
	}
	for (int i = 0; i < digit[numb].size(); i++) {
		num[digit[numb][i] - 'A'] ++;
		tot++;
	}
}

int main() {
	int t;
	scanf("%d",&t);
	for (int ii = 1; ii <= t; ii++) {
		printf("Case #%d: ",ii);
		string a;
		cin>>a;
		memset(num, 0, sizeof(num));
		int len = a.size();
		int tot = 0;
		for (int i = 0; i < len; i++) {
			num[a[i] - 'A']++;
			tot++;
		}
		flag = 0;
		for (int i = 0; i < 10; i++) {
			dfs(0, i, tot);
		}
		cout<<ans<<endl;
	}
}