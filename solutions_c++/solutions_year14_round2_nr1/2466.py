// Syed Ghulam Akbar
// CodeJam 2014 - Round 1B

#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <math.h> 
#include <vector>

using namespace std;

struct compare {
    bool operator()(const string& first, const string& second) {
        return first.size() > second.size();
    }
};

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {
		int i, j, N;
		string input;
		vector<string> list;

		cin >> N;
		for (i=0; i<N; i++)
		{
			cin >> input;
			list.push_back(input);
		}

		// Sort the list by lenth
		compare c;
		std::sort(list.begin(), list.end(), c);

		string current="", compare="", newString;
		current = list[0];

		// Compare the current string with rest of the string in list
		bool possible = true;
		long changes = 0;

		for (i=1; i<N; i++)
		{
			string newString = "";
			compare = list[i];
			int x = 0;

			for (j=0; j<compare.length(); j++)
			{
				if (compare[j] != current[x])
				{
					bool secondChange = false;

					// Eat characters from the big string
					if (j > 0 && j < compare.length() && compare[j-1] == compare[j])
					{
						while (j > 0 && j < compare.length() && compare[j-1] == compare[j])
						{
							j++;
							changes++;
						}
					}

					if (compare[j] != current[x])
					{
						if (x > 0 && x < current.length() && current[x-1] == current[x])
						{
							while (x > 0 && x < current.length() && current[x-1] == current[x])
							{
								x++;
								changes++;
							}
							secondChange = true;
						}
					}

					if (j > compare.length() || x > current.length() || compare[j] != current[x])
					{
						possible = false;
						break;
					}
				}

				newString += compare[j];
				x++;
			}

			if ( x < current.length() & possible)
			{
				if (current[x-1] == current[x] )
				{
					while (x < current.length() )
					{
						x++;
						changes++;
					}
				}
				else
					possible = false;
			}

			current = newString;
		}

		cout << "Case #" << test << ": ";

		if (possible)
			cout << changes << endl;
		else
			cout << "Fegla Won" << endl;
	}
}
