#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		long long int N;
		cin >> N;
		int seen[10];
		for (int i = 0; i < 10; i++) seen[i] = 0;
		int seens = 0;
		if (N == 0)
		{
			cout << "Case #" << t << ": INSOMNIA" << endl;
			continue;
		}
		long long int ACC = N;
		while(1)
		{
			string S = to_string(ACC);
			for (int i = 0; i < S.length(); i++)
			{
				char c = S.at(i) - '0';
				if (!seen[c]) seens++;
				seen[c] = 1;
			}
			if (seens == 10)
			{
				cout << "Case #" << t << ": " << ACC << endl;
				break;
			}
			ACC += N;
		}
	}
}