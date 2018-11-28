#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int panc[1010];

int split_plate(int ind, int eating)
{
	return panc[ind] / eating - (panc[ind] % eating == 0 ? 1 : 0);
}

int main()
{
	int e, t, i, diners, spec, eat;

	int mins, maxi;

	cin >> t;

	for (e = 1; e <= t; ++e)
	{
		cin >> diners;
		maxi = 0;

		for (i = 0; i < diners; ++i)
		{
			cin >> panc[i];
			if (panc[i] > maxi)
			{
				maxi = panc[i];
			}
		}

		
		spec = 111111;
		for (eat = 1; eat <= maxi; ++eat)
		{
			mins = 0;
			for (i = 0; i < diners; ++i)
			{
				if (panc[i] > eat)
				{
					mins += split_plate(i, eat);
				}
			}

			mins += eat;

			if (mins < spec)
			{
				spec = mins;
			}
		}

		cout << "Case #" << e << ": " << spec << endl;

	}

	return 0;
}