// Author: thecodekaiser
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve(int CS)
{
	string str;
	cin >> str;

	reverse(str.begin(), str.end());

	
	int cnt = 0;
	bool flag = false;

	int N = str.length();

	for(int i = N-1; i >= 0; i--)
	{
		if(str[i] == '+')
		{
			flag = true;
		}

		if(str[i] == '-')
		{
			int j = i;

			while(j >= 0)
			{
				if(j > 0 and str[j-1] == '+')
					break;

				j--;
			}

			if(flag)
				cnt += 2;
			else
				cnt += 1, flag = true;


			i = j-1;
		}
	}

	printf("CASE #%d: %d\n", CS, cnt);

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