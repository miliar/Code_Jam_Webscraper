#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <functional>

using namespace std;

bool ascending (int *i, int *j) { return (i[0]<j[0]); }

void main()
{
	ifstream input;
	input.open("A-large.in"); // File Name Here

	if (!input.is_open())
	{
		cout << "Error opening file\n";
		system("pause");
	}

	int tot_cases;
	input >> tot_cases;

	ofstream output;
	output.open("solution.out");

	for (int i = 1; i <= tot_cases; i++)
	{
		output << "Case #" << i << ": ";

		int N = 0;
		input >> N;

		vector<int> list;
		for (int i = 0; i < N; i++)
		{
			int val = 0;
			input >> val;
			list.push_back(val);
		}

		// Case 1
		int ans1 = 0;
		for (int i = 1; i < N; i++)
		{
			if (list[i] < list[i - 1])
				ans1 += list[i - 1] - list[i];
		}

		// Case 2
		int ans2 = 0;
		int min = 0;
		for (int i = 1; i < N; i++)
		{
			int temp = 0;
			temp = list[i-1] - list[i];
			if (temp > min)
				min = temp;
		}
		for (int i = 0; i < N-1; i++)
		{
			if (list[i] > min)
				ans2 += min;
			else
				ans2 += list[i];
		}

		output << ans1 << " " << ans2 << '\n';
	}

	output.close();
	input.close();
}
