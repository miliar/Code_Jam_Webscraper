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
	fstream fin("B.in");
	fstream fout("B.out");
	int T, N;
	string s;

	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> s;
		cout << "Case #" << i << ": " << solve(s) << endl;
	}


	system("pause");
	return 0;
}