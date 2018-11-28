#include <iostream>
#include <string>
using namespace std;

int f(string& s)
{
	int cnt = 0;
	for(int i = 1; i < s.size(); ++i)
	{
		if(s[i] != s[i - 1]) ++cnt;
	}
	return cnt + (s[s.size() - 1] == '-');
}

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		string s;
		cin >> s;
		cout << "Case #" << i << ": " << f(s) << endl;
	}
	return 0;
}