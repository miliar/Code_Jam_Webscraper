#include<iostream>
#include<string>
using namespace std;
int t;
string s;
int main()
{
	cin >> t;
	for(int i = 1; i <= t; i++) {
		cin >> s;
		cout << "Case #" << i << ": ";
		int ans = 0;
		for(int i = 0; i < s.size() - 1; i++)
		if(s[i] != s[i+1]) ans++;
		if(s[s.size() - 1] == '-') ans++;
		cout << ans << endl;
	}
	return 0;
}
	
