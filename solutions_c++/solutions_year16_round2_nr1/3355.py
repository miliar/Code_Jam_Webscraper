#include <iostream>
#include <string>

using namespace std;

int main()
{
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		int cnt[26] = {0};
		int ans[10] = {0};
		string S;
		cin >> S;
		for (int j = 0; j < S.size(); j++) {
			cnt[S[j] - 'A']++;
		}
		while (cnt['z' - 'a'] > 0) {
			ans[0]++;
			cnt['z' - 'a']--;
			cnt['e' - 'a']--;
			cnt['r' - 'a']--;
			cnt['o' - 'a']--;
		}
		while (cnt['w' - 'a'] > 0) {
			ans[2]++;
			cnt['t' - 'a']--;
			cnt['w' - 'a']--;
			cnt['o' - 'a']--;
		}
		while (cnt['u' - 'a'] > 0) {
			ans[4]++;
			cnt['f' - 'a']--;
			cnt['o' - 'a']--;
			cnt['u' - 'a']--;
			cnt['r' - 'a']--;
		}
		while (cnt['x' - 'a'] > 0) {
			ans[6]++;
			cnt['s' - 'a']--;
			cnt['i' - 'a']--;
			cnt['x' - 'a']--;
		}
		while (cnt['g' - 'a'] > 0) {
			ans[8]++;
			cnt['e' - 'a']--;
			cnt['i' - 'a']--;
			cnt['g' - 'a']--;
			cnt['h' - 'a']--;
			cnt['t' - 'a']--;
		}
		while (cnt['o' - 'a'] > 0) {
			ans[1]++;
			cnt['o' - 'a']--;
			cnt['n' - 'a']--;
			cnt['e' - 'a']--;
		}
		while (cnt['h' - 'a'] > 0) {
			ans[3]++;
			cnt['t' - 'a']--;
			cnt['h' - 'a']--;
			cnt['r' - 'a']--;
			cnt['e' - 'a'] -= 2;
		}
		while (cnt['f' - 'a'] > 0) {
			ans[5]++;
			cnt['f' - 'a']--;
			cnt['i' - 'a']--;
			cnt['v' - 'a']--;
			cnt['e' - 'a']--;
		}
		while (cnt['s' - 'a'] > 0) {
			ans[7]++;
			cnt['s' - 'a']--;
			cnt['e' - 'a'] -= 2;
			cnt['v' - 'a']--;
			cnt['n' - 'a']--;
		}
		while (cnt['n' - 'a'] > 0) {
			ans[9]++;
			cnt['n' - 'a'] -= 2;
			cnt['i' - 'a']--;
			cnt['e' - 'a']--;
		}
		cout << "Case #" << i << ": ";
		for (int j = 0; j < 10; j++) {
			for (int k = 0; k < ans[j]; k++) cout << j;
		}
		cout << endl;
	}
	return 0;
}
