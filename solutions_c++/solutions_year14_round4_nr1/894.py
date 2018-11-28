#include <iostream>
#include <set>

using namespace std;

int solve()
{
	multiset<int> files;

	int n, floppySize;
	cin >> n >> floppySize;

	for(int i = 0; i < n; i++)
	{
		int file;
		cin >> file;

		files.insert(file);
	}

	int pairs = 0;

	for(auto it = files.begin(); it != files.end();)
	{
		int spaceLeft = floppySize - *it;

		auto pair = files.upper_bound(spaceLeft);
		if(pair == files.begin())
		{
			it++;
			continue;
		}
		pair--;

		if(pair != it)
		{
			auto next = it;
			next++;

			if(next == pair)
			{
				next++;
			}

			files.erase(it);
			files.erase(pair);
			pairs++;

			it = next;
		}
		else
		{
			it++;
		}
	}

	return pairs + files.size();
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": " << solve() << endl;
	}

	return 0;
}