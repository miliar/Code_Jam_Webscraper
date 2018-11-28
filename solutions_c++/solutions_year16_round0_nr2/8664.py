#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
#define sz size()
#pragma warning(disable:4996)
void reverse_n_flip(string &s,int n) {
	for (int i = 0;i <=n;i++) {
		if (s[i] == '-')s[i] = '+';
		else if (s[i] == '+')s[i] = '-';
	}
	reverse(s.begin(), s.begin() + n);
}
bool happy(string s) {
	for (int i = 0;i < s.sz;i++) {
		if (s[i] == '-')return false;
	}
	return true;
}
int main() {
	ios::sync_with_stdio(0);
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);
	int t=1;
	cin >> t;
	for (int m = 1 ;m <=t;m++)
	{
		string s;
		cin >> s;
		int c = 0;
		while (!happy(s)) {
			int i;
			for (i = 1;i <=s.sz;i++) {
				if (s[i] != s[i - 1])break;
			}
			i--;
			reverse_n_flip(s, i);
			c++;
		}
		cout<<"Case #"<<m<<": "<< c << endl;
	}
//	system("pause");
	return 0;
}