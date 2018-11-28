#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <functional>
#include <cmath>
#include <string>
#include <queue>
#include <numeric>
#include <map>
#include <set>

using namespace std;


int main(int argc, char *argv)
{
	ifstream ifs("D-large.in");
	ofstream ofs("D-large.out");
	unsigned int nb_cases;
	ifs >> nb_cases;
	for (unsigned int i = 0; i < nb_cases; i++)
	{
		ofs << "Case #"<<i+1<<": ";
		// do for each case
		size_t N;
		ifs >> N;
		vector<double> n(N);
		vector<double> k(N);
		for (size_t j = 0; j < N; j++)
			ifs >> n[j];
		for (size_t j = 0; j < N; j++)
			ifs >> k[j];
		vector<bool> k_used(N, false);
		vector<bool> n_used(N, false);
		size_t k_wins = 0;
		std::sort(n.begin(), n.end(), less<double>());
		std::sort(k.begin(), k.end(), greater<double>());
		for (size_t j = 0; j < N; j++)
		{
			size_t max_idx_k, min_idx_k;
			double min_k = 1.0, max_k = 0.0;
			for (size_t l = 0; l < N; l++)
			{
				if (!k_used[l])
				{
					if (min_k > k[l])
					{
						min_k = k[l];
						min_idx_k = l;
					}
					if (max_k < k[l])
					{
						max_k = k[l];
						max_idx_k = l;
					}
				}
			}
			if (n[j] < min_k)
			{
				k_used[max_idx_k] = true;
				k_wins++;
			}
			else if (n[j] > min_k)
			{
				k_used[min_idx_k] = true;
			}
		}
		ofs << N - k_wins << ' ';
		k_used.assign(N, false);
		double diff = std::numeric_limits<double>::max();
		
		k_wins = 0;
		for (size_t j = 0; j < N; j++)
		{
			diff = std::numeric_limits<double>::max();
			size_t used_idx;
			size_t l;
			for (l = 0; l < N; l++)
				if (!k_used[l] && (k[l] - n[j]) > 0 && diff > (k[l] - n[j]))
				{
					diff = k[l] - n[j];
					used_idx = l;
				}
			if (diff !=  std::numeric_limits<double>::max())
			{
				k_used[used_idx] = true;
				k_wins++;
			}
			else
			{
				for (l = 0; l < N; l++)
					if (!k_used[l] && (k[l] - n[j]) < 0 && diff > (k[l] - n[j]))
					{
						diff = k[l] - n[j];
						used_idx = l;
					}
					k_used[used_idx] = true;
			}
		}
		ofs << N - k_wins << ' ';
		ofs << endl;
	}
	return 0;
}