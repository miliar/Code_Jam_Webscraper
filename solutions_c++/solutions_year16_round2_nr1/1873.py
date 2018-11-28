#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int lcnt[27];
int cnt[15];
int tmp[27];
bool check(string str) {
	int sz = str.size();
	memset(tmp, 0, sizeof(tmp));
	for (int i = 0; i < sz; i++) {
		tmp[str[i]-'A']++;
	}
	bool flag = true;
	for (int i = 0; i < 26; i++) {
		if (tmp[i] > lcnt[i])
		{
			flag = false;
			break;
		}
	}
	return flag;
}
void remove(string str) {
	int sz = str.size();
	memset(tmp, 0, sizeof(tmp));
	for (int i = 0; i < sz; i++) {
		tmp[str[i]-'A']++;
	}
	bool flag = true;
	for (int i = 0; i < 26; i++) {
		lcnt[i] -= tmp[i];
	}
	return ;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tc;
	cin >> tc;
	for (int cs = 1; cs <= tc; cs++) {
		memset(cnt, 0, sizeof(cnt));
		memset(lcnt, 0, sizeof(lcnt));
		string s;
		cin >> s;
		int sz = s.size();
		for (int i = 0; i < sz; i++) {
			lcnt[s[i]-'A']++;
		}
		string str[] = {"ZERO", "TWO", "SIX", "SEVEN", "EIGHT", "FOUR", "FIVE", "ONE", "NINE", "THREE"};
		int val[] = {0,2,6,7,8,4,5,1,9,3};
		for (int i = 0; i <= 9; i++) {
			while (check(str[i]) == true) {
				cnt[val[i]]++;
				remove(str[i]);
			}
		}
		cout << "Case #" << cs << ": ";
		for (int i = 0; i <= 9; i++) {
			while (cnt[i]--) {
				cout << i;
			}
		}
		cout<<endl;


	}
	return 0;
}