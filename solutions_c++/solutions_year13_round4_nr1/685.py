#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

const long long p = 1000002013;

struct node
{
	long long num, ind;
};

bool myCompare(node n1, node n2)
{
	return (n1.ind < n2.ind);
}

int main()
{
	long long n, m, t, tt;
	vector<node> o, e;
	long long origin, opt, save, i, j, k, l;
	node s[1005];
	node temp;
	
	cin >> tt;
	
	for (t = 1; t <= tt; ++t)
	{
		cin >> n >> m;
		o.clear();
		e.clear();
		origin = 0;
		opt = 0;
		save = 0;
		for (i = 0; i < m; ++i)
		{
			cin >> j >> k >> temp.num;
			origin = (origin + (((n + n - k + j + 1) * (k - j) / 2) % p) * temp.num) % p;
			temp.ind = j;
			o.push_back(temp);
			temp.ind = k;
			e.push_back(temp);
		}
		sort(o.begin(), o.end(), myCompare);
		sort(e.begin(), e.end(), myCompare);
				
		j = 0;
		k = -1;
		for (i = 0; i < m; ++i)
		{
			while ((j < m) && (o[j].ind <= e[i].ind))
			{
				++k;
				s[k] = o[j];
				++j;
			}
			while (e[i].num > 0)
			{
				l = min(e[i].num, s[k].num);
				e[i].num = e[i].num - l;
				opt = (opt + (((n + n - e[i].ind + s[k].ind + 1) * (e[i].ind - s[k].ind) / 2) % p) * l) % p;
				if (s[k].num <= e[i].num)
					--k;
				else
					s[k].num = s[k].num - l;
			}
		}
		
		save = (origin - opt + p) % p;
		cout << "Case #" << t << ": " << save << endl;
	}

	return 0;
}
