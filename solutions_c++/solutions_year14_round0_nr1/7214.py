#include <set>
#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int l = 0; l < t; ++l)
	{
		int a, b, tmp;
		cin >> a;
		set <int> s, res;
		for (int j = 0; j < 4*(a-1); ++j)
			cin >> tmp;
		for (int j = 0; j < 4; ++j)
		{
			cin >> tmp;
			s.insert (tmp);
		}
		for (int j = 0; j < 4*(4-a); ++j)
			cin >> tmp;
		cin >> b;
		for (int j = 0; j < 4*(b-1); ++j)
			cin >> tmp;
		for (int j = 0; j < 4; ++j)
		{
			cin >> tmp;
			if (s.find (tmp) != s.end())
				res.insert (tmp);
		}
		cout << "Case #" << l+1 << ": ";
		if (res.empty())
			cout << "Volunteer cheated!" << endl;
		else if (res.size() == 1)
			cout << *res.begin() << endl;
		else cout << "Bad magician!" << endl;
		for (int j = 0; j < 4*(4-b); ++j)
			cin >> tmp;
	}
	
	return 0;
}
