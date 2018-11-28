#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;


int main()
{
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);

	unsigned int T, iter, N;
	cin >> T;
	iter = 0;
	while (iter++ < T) {
		
		double v;
		unsigned int y = 0, z = 0;
		int naomi_firstpointer = 0, naomi_lastpointer, ken_firstpointer = 0, ken_lastpointer;
		vector<double> naomi, ken;
		int i;
		cin >> N;
		for (i = 0; i < N * 2; ++i)
		{
			cin >> v;
			if (i < N) naomi.push_back(v);
			else ken.push_back(v);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		while (naomi_firstpointer < naomi.size())
		{
			//She can always lie if the naomis smallest value is higher than kens value
			if (naomi[naomi_firstpointer] > ken[ken_firstpointer])
			{
				y++;
				ken_firstpointer++;
			}
			naomi_firstpointer++;
		}

		naomi_lastpointer = naomi.size() - 1;
		ken_lastpointer = ken.size() - 1;
		//She cannot lie so the only way to win is to have highest values
		while (naomi_lastpointer >= 0)
		{
			if (naomi[naomi_lastpointer] > ken[ken_lastpointer]){
				z++;
			}
			else{
				ken_lastpointer--;
			}
			naomi_lastpointer--;
		}

		cout << "Case #" << iter << ": " << y << " " << z << endl;
	}
	return EXIT_SUCCESS;
}