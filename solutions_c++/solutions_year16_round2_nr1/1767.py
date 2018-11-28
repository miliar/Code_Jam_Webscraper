#include <bits/stdc++.h>
/*
zero six two eight three four five seven nine one
*/
using namespace std;
typedef long double ld;
typedef long long ll;
void rem(vector<int> &cnt, string word, int times){
	for(int i = 0; i < word.size(); ++i)
		cnt[word[i]-'a'] -= times;
}
int ask(vector<int> &cnt, char letter){
	return cnt[letter-'a'];
}
string solve(string s){
	vector<int> cnt(26);
	for(int i = 0; i < s.size(); ++i)
		cnt[s[i]-'A']++;
	vector<int> ans(10);
	ans[0] = ask(cnt,'z');
	rem(cnt,"zero",ans[0]);

	ans[6] = ask(cnt,'x');
	rem(cnt,"six",ans[6]);

	ans[2] = ask(cnt,'w');
	rem(cnt,"two",ans[2]);

	ans[8] = ask(cnt,'g');
	rem(cnt,"eight",ans[8]);

	ans[3] = ask(cnt,'h');
	rem(cnt,"three",ans[3]);

	ans[4] = ask(cnt,'u');
	rem(cnt,"four",ans[4]);

	ans[5] = ask(cnt,'f');
	rem(cnt,"five",ans[5]);

	ans[7] = ask(cnt,'v');
	rem(cnt,"seven",ans[7]);

	ans[9] = ask(cnt,'i');
	rem(cnt,"nine",ans[9]);

	ans[1] = ask(cnt,'o');
	rem(cnt,"one",ans[1]);

	string ret;
	for(int i = 0; i < 10; ++i)
		for(int j = 0; j < ans[i]; ++j)
			ret.push_back(i+'0');
	return ret;
}
int main(){
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; ++tc){
		cout << "Case #" << tc << ": ";
		string s;
		cin >> s;
		cout << solve(s) << '\n';
	}
}

