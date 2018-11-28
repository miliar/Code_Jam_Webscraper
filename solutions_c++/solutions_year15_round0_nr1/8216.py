#include<fstream>
#include<string.h>

using namespace std;

ifstream cin;
ofstream cout;

class soln
{
	public:

	soln(int test_case,int max,string shy)
	{
		int i = 0,no_of_ppl_clapping = 0,no_of_friends = 0;

		while(i < shy.length())
		{
			if(no_of_ppl_clapping >= i)
			{
				no_of_ppl_clapping += (shy[i] - 48);
			}
			else
			{
				no_of_friends ++;
				no_of_ppl_clapping ++;
				no_of_ppl_clapping += (shy[i] - 48);
			}

			i++;
		}

		cout << "Case #" << test_case << ": " << no_of_friends << endl;
	}
};

main()
{
	int i = 1,max,t;
	soln *obj = NULL;
	string no_of_ppl_in_shy_level;

	cin.open("A-small-attempt0.in");
	cout.open("standing_ovation.txt");
	cin >> t;

	while(i <= t)
	{
		cin >> max;
		cin >> no_of_ppl_in_shy_level;

		obj = new soln(i,max,no_of_ppl_in_shy_level);
		i++;
	}

	return 0;
}
