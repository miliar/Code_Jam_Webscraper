// Author: thecodekaiser 
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve(int CS)
{
	int N, J;

	cin >> N >> J;

	vector<char> str(N);

	for(int i = 0; i < N; i++)
		str[i] = '0';

	str[N-1] = str[N-2] = str[0] = str[1] = '1';

	printf("CASE #%d:\n", CS);

	int mx = (N-4)/2;
	int cnt = 0;

	for(int mask = 0; mask < (1 << mx) and cnt < J; mask++, cnt++)
	{
		vector<char> temp = str;

		for(int bit = 0; bit < mx; bit++)
		{
			if(mask & (1 << bit))
			{
				int pos = bit * 2 + 2;
				temp[pos] = temp[pos+1] = '1';
			}
		}

		for(int i = 0; i < N; i++)
			cout << temp[i];
		cout << " ";
		for(int i = 2; i <= 10; i++)
			cout << i+1 << " ";
		cout << endl;
	}


	//cout << cnt << endl;
	


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