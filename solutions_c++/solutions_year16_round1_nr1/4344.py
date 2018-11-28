#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
#define sz size()
#define pb(a) push_back(a)
#define pp	pop_back()
#pragma warning(disable:4996)

int main() {
	ios::sync_with_stdio(0);
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);
	int t=1;
	cin >> t;
	for (int m = 1 ;m <=t;m++)
	{
		string s,ss;
		cin >> s;
		ss.pb(s[0]);
		char max_c=s[0];
		for (int i = 1;i < s.sz;i++) {
			if (max_c <= s[i]) {
				ss.insert(ss.begin(), s[i]);
				max_c = s[i];
			}
			else ss.pb(s[i]);
		}
		cout<<"Case #"<<m<<": "<< ss << endl;
	}
//	system("pause");
	return 0;
}