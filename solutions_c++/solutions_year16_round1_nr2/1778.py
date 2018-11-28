#include<iostream>
#include<cstdio>
#include<set>
#include<cstdlib>
#include<vector>
#include<algorithm>
using namespace std;

#define FOR(x,N) for(int x = 0 ; x < (N) ; x++ )

int main()
{
	long long T,N;
	char buf[1000000];
	freopen("in2.in", "rt", stdin);
	freopen("out2.txt", "wt", stdout);

	cin >> T;
	vector<int> num,sol;


	FOR(i, T)
	{

		cin >> N;
		int r = 2 * N*N - N;
		num.clear();
		sol.clear();
		num.resize(r);
		sol.reserve(N);


		for (int j = 0; j < r; j++)
		{
			cin >> num[j];
		}

		sort(num.begin(), num.end());

		int counter = 0;
		FOR(j, r)
		{
			if (j == 0 || num[j] == num[j - 1])
			{
				counter++;
			}
			else if (counter % 2 == 1)
			{
				sol.push_back(num[j - 1]);
				counter = 1;
			}
			else
			{
				counter = 1;
			}

			if (j == r - 1 && num[j] != num[j - 1])
			{
				sol.push_back(num[j]);
			}

		}
		sort(sol.begin(), sol.end());
		

		cout << "Case #" << i + 1 << ": ";
		
		FOR(l, sol.size())
		{
			cout << sol[l] << ' ';
		}
		cout << endl;

	}

	return 0;
}
