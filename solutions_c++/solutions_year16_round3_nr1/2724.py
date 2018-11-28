
#include <iostream>

#include <vector>
#include <map>
#include <functional>

using namespace std;

typedef long long ll;

char ToLetter(int i)
{
	char m = 'A';
	return m + i;
}

int main()
{
//	vector<int> membersNum;

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		int N;
		cin >> N;
		
		multimap<int, int, greater<int>> order;
//		int s = 0;
//		membersNum.resize(N);
		for (int k = 0; k < N; ++k)
		{
			int nb;
			cin >> nb;
//			membersNum[k] = nb;
//			s += nb;

			order.insert(pair<int,int>(nb, k));
		}

		cout << "Case #" << t << ':';

		while (order.begin()->first > 1)
		{
			cout << ' ';

			multimap<int, int>::iterator it = order.begin();
			multimap<int, int>::iterator it2 = it; ++it2;

			pair<int, int> memb1 = *it;
			pair<int, int> memb2 = *it2;
			int d = memb1.first - memb2.first;
			if (d > 0)
			{
				if (d > 2)
					d = 2;
				for (int i = 0; i < d; ++i)
				{
					cout << ToLetter(memb1.second);
				}
				memb1.first -= d;

				order.erase(it);
				order.insert(memb1);
			}
			else
			{
				cout << ToLetter(memb1.second);
				cout << ToLetter(memb2.second);
				memb1.first -= 1;
				memb2.first -= 1;

				order.erase(it);
				order.insert(memb1);

				order.erase(it2);
				order.insert(memb2);
			}
		}

		if ((order.size() & 1) != 0)
		{
			multimap<int, int>::iterator it = order.begin();

			cout << ' ';
			cout << ToLetter(it->second);
			order.erase(it);
		}
		while (!order.empty())
		{
			multimap<int, int>::iterator it = order.begin();
			multimap<int, int>::iterator it2 = it; ++it2;

			cout << ' ';
			cout << ToLetter(it->second);
			cout << ToLetter(it2->second);

			order.erase(it);
			order.erase(it2);
		}

		cout << endl;
	}

	return 0;
}
