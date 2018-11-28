#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int compute_wins(vector<double> naomi, vector<double> ken, int N)
{
	int wins = 0;
	vector<bool> used;
	for (int j = 0; j < N; j++)
		used.push_back(false);

	for (int j = N - 1; j >= 0; j--)
	{
		int k;
		for (k = 0; k < N; k++)
		{
			if (used[k] == false)
			{
				if (ken[k] > naomi[j])
					break;
			}
		}
		if (k == N)
		{
			wins++;
			int front = 0;
			while (used[front] == true)
				front++;
			used[front] = true;
		}
		else
			used[k] = true;			
	}
	return wins;
}

int main()
{
	int ncases;
	cin >> ncases;
	for (int i = 1; i <= ncases; i++)
	{
		int N;
		cin >> N;
		vector<double> naomi;
		vector<double> ken;
		for (int j = 0; j < N; j++)
		{
			double temp;
			cin >> temp;
			naomi.push_back(temp);
		}
		for (int j = 0; j < N; j++)
		{
			double temp;
			cin >> temp;
			ken.push_back(temp);
		}
		
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int normal_wins = compute_wins(naomi, ken, N);
		int deceit_wins = N - compute_wins(ken, naomi, N);

		cout << "Case #" << i << ": " << deceit_wins << " " << normal_wins << "\n";
	}
	return 0;
}