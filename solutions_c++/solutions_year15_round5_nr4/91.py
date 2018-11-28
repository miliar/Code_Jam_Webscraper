#include <bits/stdc++.h>
using namespace std;

vector <long long> have;
map <long long, long long> num;

bool check(long long d)
{
	map <long long, long long> t = num;
	for(int i = 0; i < have.size(); i++)
	{
		long long amount = t[have[i]];
		if(amount > 0)
		{
			if(t[have[i] + d] < amount)
				return false;
			t[have[i] + d] -= amount;
		}
	}
	return true;
}

void update(long long d)
{
	vector <long long> nextHave;
	map <long long, long long> nextNum;
	map <long long, long long> t = num;
	for(int i = 0; i < have.size(); i++)
	{
		long long amount = t[have[i]];
		if(amount > 0)
		{
			if(have[0] != 0)
			{
				nextHave.push_back(have[i] + d);
				nextNum[have[i] + d] = amount;
			}
			else
			{
				nextHave.push_back(have[i]);
				nextNum[have[i]] = amount;
			}

			t[have[i] + d] -= amount;
		}
	}
	have = nextHave;
	num = nextNum;

}

bool checkZero()
{
	for(int i = 0; i < have.size(); i++)
		if(num[have[i]] % 2 != 0)
			return false;
	return true;
}

void updateZero()
{
	for(int i = 0; i < have.size(); i++)
		num[have[i]] /= 2;
}

long long calc()
{
	if(have[0] == 0)
	{
		if(checkZero())
		{
			updateZero();
			return 0;
		}
	}
	if(have[0] == 0)
	{
		for(int i = 1; i < have.size(); i++)
		{
			long long d = have[i] - have[0];
			if(check(d))
			{
				long long ret;
				if(have[0] == 0)
					ret = d;
				else
					ret = -d;
				update(d);
				return ret;
			}
		}
	}
	else
	{
		for(int i = have.size()-1; i >= 1; i--)
		{
			long long d = have[i] - have[0];
			if(check(d))
			{
				long long ret;
				if(have[0] == 0)
					ret = d;
				else
					ret = -d;
				update(d);
				return ret;
			}
		}
	}
	return 0;
}

void solve()
{
	int n;
	long long sum = 0;
	cin >> n;
	have.clear();
	num.clear();
	for(int i = 1; i <= n; i++)
	{
		long long t;
		cin >> t;
		have.push_back(t);
	}
	for(int i = 1; i <= n; i++)
	{
		long long x;
		cin >> x;
		num[have[i-1]] = x;
		sum += x;
	}
	while(sum > 1)
	{
		sum /= 2;
		long long ans = calc();
		
		cout << ans << (sum > 1 ? " " : "\n");
	}
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
