#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int num_cases;
	cin >> num_cases;
	for (int case_num = 1; case_num <= num_cases; ++case_num)
	{
		int s_max;
		cin >> s_max;
		string v;
		cin >> v;
		//cout << s_max << endl << v << endl;

		int min_add = 0;
		int total_stand = 0;
		for (int i = 0; i <= s_max; ++i)
		{
			if (v[i] != '0')
			{
				if ((total_stand + min_add) < i)
					min_add = i - total_stand;
				total_stand += int(v[i] - '0');
			}
		}
		cout << "Case #" << case_num << ": " << min_add << endl;
	}
	return 0;
}