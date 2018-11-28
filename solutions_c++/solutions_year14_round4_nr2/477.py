#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

struct node
{
	int ind, v;
};

bool compare(node n1, node n2)
{
	return n1.v < n2.v;
}

int main()
{
	int t;
	cin >> t;
	
	for (int tt = 1; tt <= t; ++tt)
	{
		int n, res = 0, l, r;
		node tn;
		vector<node> a;
		int u[1005];
		
		cin >> n;
		
		for (int i = 0; i <= n + 1; ++i)
			u[i] = 1;
		
		for (int i = 1; i <= n; ++i)
		{
			tn.ind = i;
			cin >> tn.v;
			a.push_back(tn);
		}
		
		sort(a.begin(), a.end(), compare);
		
		for (int i = 0; i < n; ++i)
		{
			u[a[i].ind] = 0;
			l = 0;
			r = 0;
			for (int j = a[i].ind; j > 0; --j)
				l += u[j];
			for (int j = a[i].ind; j <= n; ++j)
				r += u[j];
			res += min(l, r);
		}
		
		cout << "Case #" << tt << ": " << res << endl;
	}

	return 0;
}
