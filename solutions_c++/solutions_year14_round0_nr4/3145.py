#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	float *Naomi;
	float *Ken;
	vector<float>vKen;
	for (int i = 1; i <= t; i++)
	{
		int n;
		cin >> n;
		Naomi = new float[n];
		Ken = new float[n];
		vKen.clear();
		for (int j = 0; j < n; j++)
			cin >> Naomi[j];
		sort(Naomi, Naomi + n);
		
		for (int j = 0; j < n; j++)
		{
			cin >> Ken[j];
			vKen.push_back(Ken[j]);
		}
		sort(Ken, Ken + n);
		sort(vKen.begin(), vKen.end());
		int score_d = 0, score_w = 0;
		int start = 0, end;
		int start_n = 0, start_k = 0;
		while (start_n < n)
		{
			while (start_n < n && Naomi[start_n] < Ken[start_k])
			{
				start_n++;
			}
			while (start_n < n && Naomi[start_n] > Ken[start_k])
			{
				start_n++;
				start_k++;
				score_d++;
			}
		}
		end = n - 1;
		vector<float>::iterator it;
		int j = 0;
		bool change = false;
		while (j < n && Naomi[end] > Ken[start])
		{
			it = vKen.end() - 1;
			change = false;
			if (*it > Naomi[end])
			{
				while (*it > Naomi[end] && it != vKen.begin())
				{
					it--;
					change = true;
				}
				if (change)
					it++;
				end--;
				vKen.erase(it);
			}
			else
			{
				start++;
				score_w++;
				vKen.erase(vKen.begin());
				end--;
			}
			j++;
		}

		cout << "Case #" << i << ": " << score_d << " " << score_w << endl;
		delete [] Naomi;
		delete [] Ken;
	}
	return 0;
}