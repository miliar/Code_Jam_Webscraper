
#include <string>
#include <iostream>
using namespace std;

int main()
{
	int cases, parties, sum;
	int number[26];

	string solution = "";
	
	
	cin >> cases;
	for (int c = 1; c <= cases; c++)
	{
		cin >> parties;
		sum = 0;
		for (int p = 0; p < parties; p++)
		{
			cin >> number[p];
			sum += p;
		}

		solution = "";
		while (sum != 0)
		{
			int max = 0;
			int equal_max = -1;
			for (int p = 1; p < parties; p++)
			{
				if (number[p] > number[max])
				{
					max = p;
					equal_max = -1;
				}
				if (number[p] == number[max])
				{
					equal_max = p;
				}
			}

			if (equal_max == -1)
			{
				number[max]--;
				number[max]--;
				solution = solution +" "+char(max + 65)+char(max + 65);
			}
			else
			{
				
				if (parties % 2 == 1 && sum == parties)
				{
					number[max]--;
					solution = solution + " " + char(max + 65);
				}
				else
				{
					number[max]--;
					number[equal_max]--;
					solution = solution + " " + char(max + 65) + char(equal_max + 65);
				}
			}



			sum = 0;
			for (int p = 0; p < parties; p++)
			{
				sum += number[p];
			}
		}

		
			cout << "Case #" << c << ": " << solution << endl;
			
		
	}
	return 0;
}

