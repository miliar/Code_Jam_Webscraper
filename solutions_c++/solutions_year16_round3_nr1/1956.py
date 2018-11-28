#include <iostream>
#include <set>
#include <limits.h>
using namespace std;

#define FOR(i, s, n) for(unsigned long long i = (s); i < (n); i++)
#define pl(x) cout << x << endl

void main()
{
	int T, N, evacuadted;
	double sen[26];
	double sum;

	cin >> T;
	FOR(cases, 1, T + 1)
	{
		cin >> N;
		sum = 0;
		evacuadted = 0;
		for (int i = 0; i < N; i++)
		{
			cin >> sen[i];
			sum += sen[i];
		}

		cout << "Case #" << cases << ": ";

		while (sum > 0)
		{
			int maxId = 0;
			for (int i = 1; i < N; i++)
			{
				if (sen[i] > sen[maxId])
					maxId = i;
			}
			cout << (char)(maxId + 65);
			sen[maxId]--;
			if (sen[maxId] == 0)
				evacuadted++;
			sum--;

			if (evacuadted == N - 2 && N > 2)
			{
				cout << ' ';
				continue;
			}
				

			maxId = 0;
			for (int i = 1; i < N; i++)
			{
				if (sen[i] > sen[maxId])
					maxId = i;
			}
			cout << (char)(maxId + 65);
			sen[maxId]--;
			if (sen[maxId] == 0)
				evacuadted++;
			sum--;

			cout << ' ';
		}	
		cout << endl;
	}
}