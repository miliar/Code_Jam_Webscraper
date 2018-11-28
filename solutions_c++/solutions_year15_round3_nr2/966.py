#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int number_of_occurences(string big, string small, int size_big, int size_small)
{
	int occurences = 0;
	for (int i = 0; i < size_big - size_small + 1; i++)
	{
		bool match = true;
		for (int j = 0; j < size_small; j++)
		{
			if (big[i + j] != small[j])
			{
				match = false;
				break;
			}
		}

		if (match)
		{
			occurences += 1;
		}
	}

	return occurences;
}

int K, L, S;
int bananas_needed = 0;
int money_typings = 0;
int bananas_given = 0;
string dictionary;
string target;

string bananas_needed_string;

void back_bananas_needed(int level)
{
	for (int i = 0; i < K; i++)
	{
		bananas_needed_string[level] = dictionary[i];

		if (level == S - 1)
		{
			int occurences = number_of_occurences(bananas_needed_string, target, S, L);
			if (occurences > bananas_needed)
			{
				bananas_needed = occurences;
			}

			money_typings += 1;
			bananas_given += occurences;
		}
		else
		{
			back_bananas_needed(level + 1);
		}
	}
}

void back_bananas_given(int level)
{

}

int main()
{
	int T; cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> K >> L >> S;
		cin >> dictionary >> target;
		
		for (int i = 0; i < S; i++)
		{
			bananas_needed_string.push_back('A');
		}

		bananas_needed = 0;
		money_typings = 0;
		bananas_given = 0;
		back_bananas_needed(0);

		double result = bananas_needed - ((double)(bananas_given) / money_typings);

		if (result == (double)((int)(result)))
		{
			cout << setprecision(7) << "Case #" << t + 1 << ": " << result << ".0" << '\n';
		}
		else
		{
			cout << setprecision(7) << "Case #" << t + 1 << ": " << result << '\n';
		}
	}

	return 0;
}