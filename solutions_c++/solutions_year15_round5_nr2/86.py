#include <bits/stdc++.h>
using namespace std;

int n, d;
long long x[1001];
long long delta[1001];
long long s;

long long calc(int p)
{
	long long minV = 0, maxV = 0, v = 0;
	while(p <= n-d)
	{
		v += delta[p];
		p += d;
		minV = min(minV, v);
		maxV = max(maxV, v);
	}
	s += -minV;
	return maxV - minV;
}

void solve()
{
	s = 0;
	cin >> n >> d;
	for(int i = 1; i <= n-d+1; i++)
		cin >> x[i];
	for(int i = 1; i <= n-d; i++)
		delta[i] = x[i+1] - x[i];
	vector<long long> vals;

	for(int i = 1; i <= d; i++)
		vals.push_back(calc(i));
	sort(vals.begin(), vals.end());
	//for(int i = 0; i < d; i++)
	//	cout << vals[i] << endl;
	long long ans = vals[vals.size()-1];
	long long able = 0;
	for(int i = 0; i < vals.size(); i++)
		able += ans - vals[i];
	long long dist = x[1] - s;
	dist %= d;
	dist += d;
	dist %= d;
	s %= d;
	s += d;
	s %= d;

	if(able < dist)
		ans ++;
	cout << ans << endl;
	
}

int MAIN()
{
	int TestCase;
	cin >> TestCase;
	for(int caseID = 1; caseID <= TestCase; caseID ++)
	{
		cout << "Case #" << caseID << ": ";
		solve();
	}
	return 0;
}

int main()
{
	int start = clock();
	#ifdef LOCAL_TEST
		freopen("in.txt", "r", stdin);
		freopen("out.txt", "w", stdout);
	#endif
	ios :: sync_with_stdio(false);
	cout << fixed << setprecision(16);
	int ret = MAIN();
	#ifdef LOCAL_TEST
		cout << "[Finished in " << clock() - start << " ms]" << endl;
	#endif
	return ret;
}
