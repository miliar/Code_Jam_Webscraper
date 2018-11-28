#include <iostream>
#include <vector>
#include <string.h>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

const long long md = 1000002013;
const int MAXN = 2100;

inline long long Tri(long long n)
{
	return n * (n - 1) / 2 % md;
}

map <long long, long long> mp, np;
long long oo[MAXN], ee[MAXN], pp[MAXN];
vector <long long> vr, vs;

long long Work()
{
	int n, m;
	cin >> n >> m;
	long long ans = 0;
	vs.clear();
	vr.clear();
	mp.clear();
	np.clear();
	for (int i = 0; i < m; i ++)
	{
		cin >> oo[i] >> ee[i] >> pp[i];
		ans += (md - pp[i] * Tri(ee[i] - oo[i]) % md);
		if (ans >= md)
			ans -= md;	
		mp[oo[i]] += pp[i];
		mp[ee[i]] -= pp[i];
	}

	for (map<long long, long long>::iterator iter = mp.begin(); iter != mp.end(); iter ++)
	{
		vr.push_back(iter->first);
		vs.push_back(iter->second);
	}


	while (true)
	{
		int x = -1;
		for (int i = 0; i < vs.size(); i ++)
			if (vs[i])
			{
				x = i;
				break;
			}
		if (x == -1)  break;
		
		long long sum = 0, mn = -1, pr;
		for (int i = x; i < n; i ++)
		{
			sum += vs[i];
			if (sum == 0) 
			{			
				vs[x] -= mn;
				vs[i] += mn;
				ans += mn * Tri(vr[i] - vr[x]) % md;
				break;
			}
			if (mn == -1)
				mn = sum;
			else
				mn = min(mn, sum);
		}

	}

	return ans % md;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-output.txt", "w", stdout);
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt ++)
		cout << "Case #" << tt << ": " << Work() << endl;
	return 0;
}