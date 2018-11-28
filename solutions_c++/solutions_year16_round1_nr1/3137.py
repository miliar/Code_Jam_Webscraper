#include <iostream>
#include <algorithm>
#include <string>
#include <list>
using namespace std;

typedef long long ll;

int main(void)
{

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);
	int T = 0;
	cin >> T;
	string str;
	list<char> res;
	
	for (int i = 0; i < T; ++i)
	{
		cin >> str;
		res.clear();

		size_t sz = str.size();
		if (sz)
			res.push_back(str.at(0));

		for (int j = 1; j < sz; ++j)
		{
			if (str.at(j) >= (*res.begin()))
			{
				res.push_front(str.at(j));
			}
			else
			{
				res.push_back(str.at(j));
			}
		}

		list<char>::iterator beg, end;
		beg = res.begin();
		end = res.end();

		cout << "Case #" << i + 1 << ": ";
		for (; beg != end; ++beg)
		{
			cout << *beg;
		}
		cout << endl;
	}

	return 0;
}
