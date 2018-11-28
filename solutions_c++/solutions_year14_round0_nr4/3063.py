#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

unsigned calculateStdResult(vector <float> &naomi, vector <float> &ken)
{
	unsigned naomiWin = 0;
	unsigned kenMax = ken.size() - 1;

	for(int i =  naomi.size() - 1; i >= 0; i--)
	{
		// Find the next bigger one from Ken
		if (naomi[i] < ken[kenMax])
		{
			kenMax--;
		} else 
		{
			naomiWin++;
		}
	}

	return naomiWin;
}

unsigned calculateCheatResult(vector <float> &naomi, vector <float> &ken)
{
	unsigned kenMax = ken.size() - 1;
	unsigned kenMin = 0;
	unsigned naomiMax = naomi.size() - 1;
	unsigned naomiMin = 0;
	unsigned naomiWin = 0;

	while(naomiMax >= naomiMin)
	{
		if (naomi[naomiMax] < ken[kenMax])
		{
			kenMax--;
			naomiMin++;
		} else if (naomi[naomiMin] < ken[kenMin])
		{
			kenMax--;
			naomiMin++;
		} else 
		{
			naomiMin++;
			kenMin++;
			naomiWin++;
		}
	}

	return naomiWin;
}

int main(int argc, char *argv[])
{
	unsigned nrTCs;
	cin >> nrTCs;

	for(unsigned i = 0; i < nrTCs; i++)
	{
		unsigned N = 0;
		cin >> N;
		vector <float> naomi;
		vector <float> ken;

		for(unsigned j = 0; j < N; j++)
		{
			float inp;
			cin >> inp;
			naomi.push_back(inp);
		}

		for(unsigned j = 0; j < N; j++)
		{
			float inp;
			cin >> inp;
			ken.push_back(inp);
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		unsigned stdResult = calculateStdResult(naomi, ken);
		unsigned cheatResult = calculateCheatResult(naomi, ken);

		cout << "Case #" << (i + 1) << ": " << cheatResult << " " << stdResult << "\n";
	}

	return 0;
}