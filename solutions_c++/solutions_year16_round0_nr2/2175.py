#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define cin fin
#define cout fout
ifstream fin("a.in");
ofstream fout("ans.txt");


int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		string s;
		cin >> s;
		cout << "Case #" << t << ": ";
		int ans = 0;
		for(int i = 1; i < s.length(); i++)
		{
			if(s[i] != s[i - 1])
				ans++;
		}
		if(s[s.length() - 1] != '+')
			ans++;
		cout << ans << endl;
	}
	return 0;
}

