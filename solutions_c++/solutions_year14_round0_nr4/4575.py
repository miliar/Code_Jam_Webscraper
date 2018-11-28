#include <iostream>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

	int total_test_case;
	cin >> total_test_case;
	for (int current_case_index = 1; current_case_index <= total_test_case; current_case_index++)
	{
		int length_array;
		double wood_naomi[1000], wood_ken[1000];
		cin >> length_array;
		for (int wood_index = 0; wood_index < length_array; wood_index++)
			cin >> wood_naomi[wood_index];
		for (int wood_index = 0; wood_index < length_array; wood_index++)
			cin >> wood_ken[wood_index];

		sort(wood_naomi, wood_naomi + length_array);
		sort(wood_ken, wood_ken + length_array);

		int ken_index = length_array - 1;
		int normal_value = 0, cheated_value = 0;

		for(int naomi_index = length_array - 1; naomi_index >= 0; naomi_index--)
		{
			if (wood_naomi[naomi_index] < wood_ken[ken_index])
				ken_index--;
			else
				normal_value++;
		}

		ken_index = 0;
		for(int naomi_index = 0; naomi_index < length_array; naomi_index++)
		{
			if (wood_naomi[naomi_index] >= wood_ken[ken_index])
            {
				ken_index++;
				cheated_value++;
            }
		}

		cout << "Case #" << current_case_index << ": " << cheated_value << " " << normal_value << endl;
	}
	return 0;
}
