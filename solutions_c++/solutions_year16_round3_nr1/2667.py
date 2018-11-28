#include <iostream>
#include <vector>
#include <ctime>
#include <fstream>
#include <cstring>
#include <string>
#include <algorithm>
#include <set>
#include<map>

using namespace std;


int main()
{
	fstream in("in.in"), out("out.txt");


	int T;

	in >> T;

	std::set<int>::reverse_iterator rit;

	for (int t = 1; t <= T; ++t)
	{
		int n, a;

		in >> n;

		long long sum = 0;

		vector<int> parties(n);

		for (int i = 0; i < n; ++i)
		{
			in >> a;

			sum+=a;
			parties[i] = a;
		}

		out << "Case #" << t << ": ";

		while (true)
		{
			int first = 0, first_i = -1;
			int second = 0, second_i = -1;

			for (int i = 0; i < n; ++i)
				if (parties[i] > first)
				{
					first = parties[i];
					first_i = i;
				}

			bool used = 0;

			for (int i = 0; i < n; ++i)
			{
				if (parties[i] > second)
				{
					if (parties[i] == first && !used)
					{
						used = 1;
						continue;
					}

					second = parties[i];
					second_i = i;
				}

			}

			if (first <= 0 || second <= 0) 
			{
				cout << t << endl;
				break;
			}

			char let1 = (char)(first_i + 'A');
			char let2 = (char)(second_i + 'A');

			if (first - 1 >= 0 && second - 1 >= 0 && (first - 1) <= (sum - 2) / 2 && (second - 1) <= (sum - 2) / 2 && sum - 2 != 1)
			{
				out << let1 << let2 << " ";

				parties[first_i] -= 1;
				parties[second_i] -= 1;

				sum -= 2;
			}
			else if (first - 2 >= 0 && second <= (sum - 2) / 2)
			{
				out << let1 << let1 << " ";

				parties[first_i] -= 2;

				sum -= 2;
			} 
			else if (first - 1 >= 0 && second <= (sum - 1) / 2) 
			{
				out << let1 << " ";

				sum -= 1;

				parties[first_i] -= 1;
				
			}
			else
			{
				out << let2 << " ";

				parties[second_i] -= 1;
				sum -= 1;
			}
		}

		out << endl;
	}

	in.close();
	out.close();

	return 0;
}