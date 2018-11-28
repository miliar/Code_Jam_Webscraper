#include <fstream>
#include <algorithm>
#include <set>
using namespace std;
int T, n, G, v[10100], sol;
multiset <int> S;

int main()
{
	int t, i;
	multiset <int>::iterator it;
	ifstream fin("A.in");
	ofstream fout("A.out");
	fin >> T;
	for(t = 1; t <= T; ++t)
	{
		fin >> n >> G;
		for(i = 1; i <= n; ++i)
		{
			fin >> v[i];
			S.insert(v[i]);
		}
		S.insert(1000000000);
		sol = 0;
		sort(v + 1, v + n + 1);
		for(i = n; i > 0; --i)
		{
			it = S.lower_bound(v[i]);
			if(*it == 1000000000 || *it != v[i])
				continue;
			S.erase(S.find(v[i]));
			sol++;
			it = S.upper_bound(G - v[i]);
			if(it != S.begin())
			{
				it--;
				S.erase(S.find(*it));
			}
		}
		S.clear();
		fout << "Case #" << t << ": " << sol << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}
