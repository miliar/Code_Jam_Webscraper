#include <bits/stdc++.h>
using namespace std;

string nums[] = {"ZERO","ONE","TWO","THREE","FOUR",
	"FIVE","SIX","SEVEN","EIGHT","NINE"};

int lcount[10][26];

void getLetterCount() {
	for (int i=0; i<10; i++) {
		for (int j=0; j<nums[i].size(); j++)
			lcount[i][nums[i][j]-'A']++;
	}
}

int cnt[26];
void subtractDigits(int dig) {
	for (int i=0; i<26; i++)
		cnt[i]-=lcount[dig][i];
}

int main() {
	getLetterCount();
	int T; scanf("%d",&T);
	for (int tt=1; tt<=T; tt++) {
		string S; cin >> S;
		fill(cnt,cnt+26,0);
		for (int i=0; i<S.size(); i++)
			cnt[S[i]-'A']++;

		vector<int> digits;
		vector<char> chrs = {'Z','X','W','U','G','H','F','O','S','I'};
		vector<int> digs = {0,6,2,4,8,3,5,1,7,9};
		for (int i=0; i<chrs.size(); i++) {
			int times = cnt[chrs[i]-'A'];
			for (int j=0; j<times; j++) {
				subtractDigits(digs[i]);
				digits.push_back(digs[i]);
			}
		}

		sort(digits.begin(),digits.end());
		printf("Case #%d: ",tt);
		for (int i=0; i<digits.size(); i++)
			printf("%d",digits[i]);
		printf("\n");
		for (int i=0; i<26; i++)
			assert(cnt[i] == 0);
	}
	return 0;
}