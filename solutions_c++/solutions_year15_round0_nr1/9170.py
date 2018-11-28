#include<fstream>
#include<string.h>

using namespace std;

ifstream in;
ofstream out;

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

		out << "Case #" << test_case << ": " << no_of_friends << endl;
	}
};

main()
{
	int i = 1,max,t;
	soln *obj = NULL;
	string no_of_ppl_in_shy_level;

	in.open("A-large.in.txt");
	out.open("ans.txt");
	in >> t;

	while(i <= t)
	{
		in >> max;
		in >> no_of_ppl_in_shy_level;

		obj = new soln(i,max,no_of_ppl_in_shy_level);
		i++;
	}

	return 0;
}
