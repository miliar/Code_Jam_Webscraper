#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";

		int N, K;
		cin >> N >> K;
		vector<double> yes(N);
		for(int i = 0; i < N; ++i)
			cin >> yes[i];

		vector<bool> choice(N, false);
		for(int i = 0; i < K; ++i)
			choice[i] = true;
		sort(choice.begin(), choice.end());

		double best = 0;

		do
		{
			vector<double> yes2;
			for(int i = 0; i < N; ++i)
				if(choice[i])
					yes2.push_back(yes[i]);

			double prob = 0;
			vector<bool> choice2(K, false);
			for(int i = 0; i < K/2; ++i)
				choice2[i] = true;
			sort(choice2.begin(), choice2.end());

			do
			{
				double singl = 1;
				for(int i = 0; i < K; ++i)
				{
					if(choice2[i])
						singl *= yes2[i];
					else 
						singl *= 1-yes2[i];
				}
				prob += singl;
			}
			while(next_permutation(choice2.begin(), choice2.end()));
			best = max(best, prob);
		}
		while(next_permutation(choice.begin(), choice.end()));

		cout << best << "\n";
	}
}
