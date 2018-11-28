#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int getSum(const int *arr, int size)
{
	int sum = 0;

	for (int i = 0; i < size; ++i)
	{
		sum += arr[i];
	}

	return sum;
}

bool checkMaj(const int *arr, const int size , const double maj)
{
	for (int i = 0; i < size; ++i)
	{
		if (arr[i] > maj)
		{
			return false;
		}
	}

	return true;
}


int main()
{
	ifstream inF;
	ofstream outF;

	inF.open("input-small.in");
	outF.open("output-small.out");

	int t;
	inF >> t;


	int *arr = new int[28];

	for (int test_cases = 1; test_cases < t + 1; ++test_cases)
	{
		outF << "Case #" << test_cases << ": ";

		int n;
		inF >> n;

		for (int s = 0; s < n; ++s)
		{
			inF >> arr[s];
		}

		int sum = 100;
		int *max = NULL;
		double new_maj = 0;
		int current_max = 0;
		while (sum != 0)
		{
			max = max_element(arr, arr + n);
			sum = getSum(arr, n);

			if (*max == 1)
			{
				// Handle final case
				int num_ones = count(arr, arr+n, 1);

				if (num_ones == 2)
				{
					int pos = distance(arr, max);
					char party = static_cast<char>(pos + 65);
					outF << party;
					--(*max);
					
					max = max_element(arr, arr + n);
					pos = distance(arr, max);
					party = static_cast<char>(pos + 65);
					outF << party;
					--(*max);
					break; // exit
				}
				else
				{
					if (num_ones % 2 == 0)
					{
						int pos = 0;
						char party;
						bool needs_space = false;
						// Go through outputting two at a time
						for (; max != arr + n; ++max)
						{
							if (*max == 1)
							{
								pos = distance(arr, max);
								party = static_cast<char>(pos + 65);
								outF << party;

								if (needs_space)
								{
									outF << " ";
									needs_space = false;
									continue;
								}
								needs_space = true;
							}
						}
					}
					else
					{
						// Output one then two at a time
						int pos = 0;
						char party;
						bool needs_space = false;

						pos = distance(arr, max);
						party = static_cast<char>(pos + 65);
						outF << party << " ";
						--(*max);

						max = max_element(arr, arr + n);

						for (; max != arr + n; ++max)
						{
							pos = distance(arr, max);
							party = static_cast<char>(pos + 65);
							outF << party;

							if (needs_space)
							{
								outF << " ";
								needs_space = false;
								continue;
							}
							needs_space = true;
						}
					}
				}
			} // max == 1

			// Case in which only two left needs handling
			if (count(arr, arr + n, 0) == (n - 2))
			{
				int *first = max;
				int val_one = *first;
				*max = 0;
				int *second = max_element(arr, arr + n);

				if (val_one != *second)
				{
					break;
				}


				char party_one = static_cast<char>(distance(arr, first) + 65);
				char party_two = static_cast<char>(distance(arr, second) + 65);
				for (int i = 0; i < *second; ++i)
				{
					outF << party_one << party_two << " ";
				}
				break;
			}



			new_maj = (sum - 2.0) / 2.0;
			current_max = *max;
			*max -= 2;

			bool can_take_2 = checkMaj(arr, n, new_maj);
			if (can_take_2)
			{
				int pos = distance(arr, max);
				char party = static_cast<char>(pos + 65);

				outF << party << party << " ";
			}
			else
			{
				int pos = distance(arr, max);
				char party = static_cast<char>(pos + 65);
				++(*max);

				outF << party << " ";
			}
		}

		max = NULL;

		outF << endl;
	}



	delete[] arr;
	inF.close();
	outF.close();

	return 0;
}
