#include<iostream>
#include<fstream>
#include<string>
#include<deque>
#include<queue>
#include<algorithm>
#include<iostream>
#include<stack>
#include<map>
#include<vector>
#include<list>
using namespace std;
#define uint unsigned int
#define ull unsigned long long
#define ll long long
#define cin fin
#define cout fout

int solve(string s)
{
	int num = s.size();
	int count = 0;
	char cur = s[0];
	for (int i = 1; i < num; i++)
	{
		if (s[i] != cur)
		{
			cur = s[i];
			count++;
		}
	}

	if (cur == '-')
		count++;
	return count;
}

int main()
{
	fstream fin("A.in");
	fstream fout("A.out");
	int T;
	string s;
	cin >> T;
	for (int k = 1; k <= T;k++)
	{
		cin >> s;
		string res;
		res += s[0];
		int num = s.size();
		for (int i = 1; i < num; i++)
		{
			if (s[i] >= res[0])
				res = s[i] + res;
			else
				res += s[i];
		}
		cout << "Case #" << k << ": " << res << endl;
	}
	system("pause");
	return 0;
}