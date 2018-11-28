#include <set>
#include <iostream>
using namespace std;

int M, N;
multiset<int> d;

void main()
{
	int tn;
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	int pn = 0;
	cin >> tn;
	while(tn --)
	{
		pn++;
		cout << "Case #" << pn << ": ";
		int res = 0;
		cin >> N >> M;
		d.clear();
		for(int i = 0; i < N; i++)
		{
			int t;
			cin >> t;
			d.insert(t);
		}
		while(d.size())
		{
			//cout << '?'<<d.size() << endl;
			int x = *d.begin();
			res ++;
			d.erase(d.begin());
			//cout << '#' << x;
			if (d.size())
			{
				auto it = d.upper_bound(M-x);
				if (it != d.begin())
				{
					--it;
					d.erase(it);
					//cout << ' ' <<*it;
				}
			}
			//cout << endl;
		}

		cout << res << endl;
	}
}
