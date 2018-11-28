#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main()
{
	auto N = 0, X = 0, Y = 0;
	cin >> N;
	vector<vector<unsigned> > m(4, vector<unsigned>(4));
	set<unsigned> original_row;
	set<unsigned> sol;
	for(auto i = 0; i < N; ++i)
	{
		cin >> X;
		for(auto j = 0; j < 4; ++j)
		{
			for(auto k = 0; k < 4; ++k)
			{
				cin >> m.at(j).at(k);
			}
		}

		for(auto elem : m.at(X - 1))
		{
			original_row.insert(elem);
		}

		cin >> Y;
		for(auto j = 0; j < 4; ++j)
		{
			for(auto k = 0; k < 4; ++k)
			{
				cin >> m.at(j).at(k);
			}
		}

		for(auto elem : m.at(Y - 1))
		{
			if(original_row.find(elem) != original_row.end())
			{
				sol.insert(elem);
			}
		}

		auto size = sol.size();
		cout << "Case #" << i + 1 << ": " << flush;
		if(size == 1)
		{
			cout << *sol.begin() << endl;
		}
		else if (size > 1)
		{
			cout << "Bad magician!" << endl;
		}
		else
		{
			cout << "Volunteer cheated!" << endl;
		}

		original_row.clear();
		sol.clear();
	}
	return 0;
}
