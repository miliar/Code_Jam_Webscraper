#include <iostream>
#include <string>
using namespace std;

int main()
{
	int inputs = 0;
	long long int number = 0;
	string snum = "";
	short n = 0;
	int limit;

	bool seen[10];

	cin >> inputs;

	for(int i = 0; i < inputs; i++)
	{
		for(int j = 0; j < 10; j++)
		{
			seen[j] = false;
		}

		cin >> number;

		limit = 1;

		do
		{
			snum = to_string(number * limit);

			for(int j = 0; j < snum.size(); j++)
			{
				n = snum[j] - '0';
				seen[n] = true;
			}

			limit++;

			//cout << snum << endl;

		}while((seen[0] == false || seen[1] == false || seen[2] == false || seen[3] == false || seen[4] == false || seen[5] == false ||seen[6] == false || seen[7] == false || seen[8] == false || seen[9] == false) && limit < 10000000);

		cout << "Case #" << i+1 << ": ";

		if(seen[0] == true && seen[1] == true && seen[2] == true && seen[3] == true && seen[4] == true && seen[5] == true &&seen[6] == true && seen[7] == true && seen[8] == true && seen[9] == true)
		{
			cout << snum << endl;
		}
		else
		{
			cout << "INSOMNIA" << endl;
		}
	}
	return 0;
}