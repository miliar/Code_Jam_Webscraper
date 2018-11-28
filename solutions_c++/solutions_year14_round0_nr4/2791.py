/*
	d.cpp
	Christopher Cabrera
	Deceitful War - Code Jam 2014 Qualification
*/

#include <iomanip>
#include <iostream>
#include <vector>
#include <algorithm>

std::vector<double> ken_w, naomi_w, ken_d, naomi_d;

int PlayWar()
{
	// naomi plays high to low
	// ken plays lowest to beat naomi 
	// or lowest he has if he can't beat her.

	int n_wins = 0;
	double n_play, k_play;
	while (naomi_w.size())
	{
		n_play = naomi_w.back(); // naomi plays largest block
		naomi_w.pop_back();	// remove block naomi played

		if (ken_w.back() > n_play) 	// ken can win, go that route.
		{
			std::vector<double>::iterator it;
			for (it = ken_w.begin(); it != ken_w.end(); ++it)	// walk backwards through ken's blocks
			{
				if (*it > n_play)
					break;
			}
			k_play = *(it);
			ken_w.erase(it);
		}
		else	// ken can't win, pick ken's lowest block to get rid of
		{
			k_play = ken_w.front();		// ken plays his lowest block
			ken_w.erase(ken_w.begin());	// remove block ken played
		}

		n_wins += (n_play > k_play);
	}

	return n_wins;
}

int PlayDeceitfulWar()
{
	// naomi burns blocks that cannot win ever by taking out ken's largest
	// then uses deceit to win with the rest by claiming she is playing highest
	// and taking ken's lowest blocks with her lowest that beat it.

	int n_wins = 0;
	double n_play, k_play;

	while (naomi_d.size())
	{
		if (naomi_d.front() < ken_d.front())	// naomi cannot win with her front card.
		{
			n_play = naomi_d.front();	// play lowest, claim just under ken's highest
			naomi_d.erase(naomi_d.begin());	// remove naomi's lowest.

			k_play = ken_d.back();	// ken plays his highest thinking that's all that can beat naomi.
			ken_d.erase(ken_d.end() - 1); // remove ken's highest.
		}
		else	// naomi's front card can win.
		{
			n_play = naomi_d.front();	// play lowest, claim just above ken's highest.
			naomi_d.erase(naomi_d.begin()); // remove naomi's lowest.

			k_play = ken_d.front();	// ken burns lowest thinking he can't win anyway.
			ken_d.erase(ken_d.begin()); // remove ken's lowest.
		}

		n_wins += (n_play > k_play);
	}

	return n_wins;
}

int main()
{
	int T, N, n_w_wins, n_dw_wins;
	double input;

	std::cin >> T;

	for (int t = 0; t < T; ++t)
	{
		ken_w.clear();
		ken_d.clear();
		naomi_w.clear();
		naomi_d.clear();

		std::cin >> N;
		for (int n = 0; n < N; ++n)
		{
			std::cin >> input;
			naomi_w.push_back(input);
			naomi_d.push_back(input);
		}
		std::sort(naomi_w.begin(), naomi_w.end());
		std::sort(naomi_d.begin(), naomi_d.end());


		for (int n = 0; n < N; ++n)
		{
			std::cin >> input;
			ken_w.push_back(input);
			ken_d.push_back(input);
		}
		std::sort(ken_w.begin(), ken_w.end());
		std::sort(ken_d.begin(), ken_d.end());

		n_w_wins = PlayWar();
		n_dw_wins = PlayDeceitfulWar();

		std::cout << "Case #" << t + 1 << ": " << n_dw_wins << ' ' << n_w_wins << '\n';

	}

	return 0;
}