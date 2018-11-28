#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main ()
{
	ifstream cin ( "input.txt" );
	ofstream cout ( "output.txt" );
	int t;
	cin >> t;
	int cur = 1;
	while (t--)
	{
		cout << "Case #" << cur << ": ";
		++cur;
		int n, m;
		cin >> n >> m;
		int cost_normal = 0;
		vector < pair < pair <int, int>, int > > vec (m);
		for (int i = 0; i < m; ++i)
		{
			cin >> vec [i].first.first >> vec [i].first.second >> vec [i].second;
			--vec [i].first.first;
			--vec [i].first.second;
			cost_normal += ((vec [i].first.second - vec [i].first.first)*n - (vec [i].first.second - vec [i].first.first)*(vec [i].first.second - vec [i].first.first - 1)/2)*vec [i].second;
		}
		sort (vec.begin (), vec.end ());
		vector <int> summs (n);
		for (int i = 0; i < vec.size (); ++i)
		{
			summs [vec [i].first.first] += vec [i].second;
			summs [vec [i].first.second] -= vec [i].second;
		}
		int cost_tricky = 0;
		vector <int> now (n+1, 0);
		for (int i = 0; i < summs.size (); ++i)
		{
			for (int j = 0; j < now.size (); ++j)
				if (now [j] != 0)
				{
					now [j-1] = now [j];
					now [j] =  0;
				}
			if (summs [i] > 0)
				now [n] += summs [i];
			else
			{
				int cur = summs [i];
				cur *= -1;
				for (int j = n; j >= 0; --j)
				{
					int temp = min (now [j], cur);
					cur -= temp;
					now [j] -= temp;
					if (cur == 0)
						break;
				}
			}
			for (int j = 0; j < now.size (); ++j)
				cost_tricky += now [j] * j; 
		}
		cout << cost_normal - cost_tricky << endl;
	}
}
/*1
6 2
1 3 2
4 6 1*/
/*10 2
1 7 2
6 9 1*/