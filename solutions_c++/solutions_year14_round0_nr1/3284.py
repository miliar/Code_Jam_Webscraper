#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
	{
		int f, s, n;
		set<int> fs, ss;
		// first
		cin >> f;
		for (int j = 0; j < (f-1)*4; ++j)
			cin >> n;
		for (int j = 0; j < 4; ++j)
		{
			cin >> n;
			fs.insert(n);
		}
		for (int j = 0; j < (4-f)*4; ++j)
			cin >> n;
		// second
		cin >> s;
		for (int j = 0; j < (s-1)*4; ++j)
			cin >> n;
		for (int j = 0; j < 4; ++j)
		{
			cin >> n;
			ss.insert(n);
		}
		for (int j = 0; j < (4-s)*4; ++j)
			cin >> n;
		// intersection
		set<int> both;
		set_intersection(fs.begin(),fs.end(),ss.begin(),ss.end(), std::inserter(both,both.begin()));
		// output
		if (both.size() == 0)
			cout << "Case #" << i+1 << ": Volunteer cheated!\n";
		else if (both.size() > 1)
			cout << "Case #" << i+1 << ": Bad magician!\n";
		else
			cout << "Case #" << i+1 << ": " << *(both.begin()) << "\n";
    }

    return 0;
}
