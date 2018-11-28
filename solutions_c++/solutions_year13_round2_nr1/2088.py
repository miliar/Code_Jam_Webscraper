#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Author : Ankul Garg

string getBits (int n, int N)
{
	string ret;
	while (n)
	{
		ret += (n%2)+'0';
		n = n/2;
	}
	int d = N-ret.size();
	while (d--) { ret += "0";}
	reverse(ret.begin(),ret.end());
	return ret;
}

int countZeros (string bits)
{
	int cnt = 0;
	for (int i = 0; i < bits.size(); i++)
	{
		if (bits[i] == '0')
		{
			cnt++;
		}
	}
	return cnt;
}

main()
{
	int T;
	cin >> T;

	for (int tCase = 1; tCase <= T; tCase++)
	{
		int A, N;
		cin >> A >> N;

		int Motes[N];
		for (int i = 0; i < N; i++)
		{
			cin >> Motes[i];
		}

		sort(Motes, Motes+N);
		int ans = -1;

		for (int i = 0; i < (1 << N); i++)
		{
			int curr = A;
			string bits = getBits(i, N);
			int ops = countZeros(bits);
			for (int j = 0; j < N; j++)
			{
				if (bits[j] == '1')
				{
					if (curr > Motes[j])
					{
						curr += Motes[j];
					}
					else
					{
						if (curr == 1)
						{
							ops = -1;
							break;
						}
						while (curr <= Motes[j])
						{
							curr += (curr-1);
							ops++;
						}
						curr += Motes[j];
					}
				}
			}
			if (ops == -1) continue;
			if (ans == -1 || (ans > ops))
			{
				ans = ops;
			}
		}
		cout << "Case #" << tCase << ": " << ans << "\n";
	}
}