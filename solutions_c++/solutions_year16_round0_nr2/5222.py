
#include <string>
#include <iostream>
#include <list>
#include <iterator>
using namespace std;

int main()
{
	int cases,moves;
	string plusminus;
	cin >> cases;

	for (int c = 1; c <= cases; c++)
	{
		
		cin >> plusminus;
		list<bool> pancakes;
		moves = 0;

		int i = 0;
		while (i < plusminus.length())
		{
			if (plusminus[i] == '+')
			{
				pancakes.push_back(true);
			}
			else
			{
				pancakes.push_back(false);
			}
			i++;
		}
		


		while (1)
		{
			while (1)
			{
				if (pancakes.empty() == false && pancakes.back() == true )
					pancakes.pop_back();
				else
					break;
			}

			if (pancakes.empty() == true)
				break;

			if (pancakes.front() == false)
				{

					std::list<bool>::iterator iterator;
					for (iterator = pancakes.begin(); iterator != pancakes.end(); ++iterator)
					{
						*iterator = !(*iterator);
					}
					pancakes.reverse();
					moves++;
				}
			else
			{
				int removal_count = 0;
				std::list<bool>::reverse_iterator iterator;
				
				for (iterator = pancakes.rbegin(); iterator != pancakes.rend(); ++iterator)
				{
					if (*iterator == true)
							{
								int i = 0;
								while (i < removal_count)
								{
									pancakes.pop_back();
									i++;
								}


								std::list<bool>::iterator iterator_2;
								for (iterator_2 = pancakes.begin(); iterator_2 != pancakes.end(); ++iterator_2)
								{
									*iterator_2 = !(*iterator_2);
								}
								moves++;
								break;
							}
					else
					{					
						removal_count++;
					}
					
				}

				pancakes.reverse();

				int i = 0;
				while (i < removal_count)
					{
						pancakes.push_back(false);
						i++;
					}
				

			}

		}
		cout << "Case #" << c << ": " << moves << endl;
	}
	
	
	return 0;
}