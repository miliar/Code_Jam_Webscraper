#include <iostream>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(pair<int, char> a, pair<int, char> b)
{
	return a.first < b.first;
}

int main(int argc, char* argv[])
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;

	for (int t = 0; t < T; t++)
	{
		int N;
		cin >> N;
		vector<pair<int, char>> v;
		char a = 'A';
		int sm = 0;
		int bbb = 0;
		for (int i = 0; i < N; i++)
		{	
			int tmp;
			cin >> tmp;
			v.push_back(make_pair(tmp, a + i));
			sm += tmp;
			if (tmp > 0)
				bbb++;
			//cout << tmp << " ";
		}
		cout << "Case #" << t + 1 << ": ";
		if (bbb > 2)
			for (;;)
			{
				sort(v.begin(), v.end(), cmp);
				if (v[0].first == 0 && v[N - 1].first == 0)
				{
					cout << endl;
					break;
				}

				if (v[0].first == v[N - 1].first)
				{
					for (int j = v[0].first; j > 0; j--)
						for (int e = 0; e < N; e++)
						{
							if (sm == 2)
								break;
							cout << v[e].second << " ";
							v[e].first--;
							sm--;
						}
				}

				if (sm > 2)
				{
					cout << v[N - 1].second << " ";
					v[N - 1].first--;
					sm--;
				}
				else
				{
					for (int j = 0; j < N; j++)
						if (v[j].first == 1)
							cout << v[j].second;
					cout << endl;
					break;
				}
			}
		else
		{
			int a1, a2;
			for (int i = 0; i < N; i++)
				if (v[i].first > 0)
				{
					a1 = i;
					break;
				}
			for (int i = a1 + 1; i < N; i++)
				if (v[i].first > 0)
				{
					a2 = i;
					break;
				}


			for (;;)
			{
				if (v[a1].first > v[a2].first)
				{
					cout << v[a1].second << " ";
					v[a1].first--;
				}
				else if (v[a2].first > v[a1].first)
				{
					cout << v[a2].second << " ";
					v[a2].first--;
				}
				else
					break;
			}

			for (int i = v[a1].first; i > 0; i--)
				cout << v[a1].second << v[a2].second << " ";
			cout << endl;
		}

	}
	return 0;
}