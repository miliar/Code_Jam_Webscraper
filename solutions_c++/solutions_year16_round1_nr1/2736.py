// Author: thecodekaiser
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve(int CS)
{
	string str;
	cin >> str;

	int len = str.length();

	deque<char> svec;

	svec.push_back(str[0]);

	for(int i = 1; i < len; i++)
	{
			if(str[i] >= svec.front())
				svec.push_front(str[i]);
			else
				svec.push_back(str[i]);
	}

	printf("CASE #%d: ", CS);
	while(!svec.empty())
	{
		cout << svec.front();
		svec.pop_front();
	}

	printf("\n");



	return;
}

int main()
{
	int t, CS = 1;
	cin >> t;

	while(t--)
		solve(CS++);

	return 0;
}