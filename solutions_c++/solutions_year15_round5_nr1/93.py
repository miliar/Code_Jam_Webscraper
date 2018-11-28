#include <bits/stdc++.h>
using namespace std;

int n, d;
int vv[1000001];
int lowbit(int x){return x&(-x);}
int query(int x)
{
	int ret = 0;
	while(x)
	{
		ret += vv[x];
		x -= lowbit(x);
	}
	return ret;
}
void update(int x, int v)
{
	//if(n == 14 && d == 489)
	//	cout << "update " << x << " " << v << endl;
	while(x <= 1000000)
	{
		vv[x] += v;
		x += lowbit(x);
	}
}

struct node
{
	int index;
	int salary;
	bool operator <(node that)const
	{
		return salary > that.salary;
	}
}N[1000001];

int toSalary[1000001];

vector <int> son[1000001];
long long s, as, cs, rs;
long long m, am, cm, rm;
bool alreadyDeleted[1000001];

int t[1000001];

void delIt(int p)
{
	/*if(n == 14 && d == 489)
	cout << "p = " << p << endl;*/
	if(alreadyDeleted[p]) return;
	alreadyDeleted[p] = true;
	update(t[p], -1);
	for(int i = 0; i < son[p].size(); i++)
		delIt(son[p][i]);
}



void solve()
{
	memset(alreadyDeleted, 0, sizeof(alreadyDeleted));
	memset(vv, 0, sizeof(vv));

	

	cin >> n >> d;
	cin >> s >> as >> cs >> rs;
	cin >> m >> am >> cm >> rm;
	for(int i = 1; i <= n; i++)
		son[i].clear();
	N[1].index = 1;
	N[1].salary = s + 1;
	t[1] = s + 1;
	for(int i = 2; i <= n; i++)
	{
		s = (s * as + cs) % rs;
		m = (m * am + cm) % rm;
		N[i].index = i;
		N[i].salary = s + 1;
		son[m%(i-1) + 1].push_back(i);
		t[i] = min(t[m%(i-1) + 1], N[i].salary);
	}
	//if(n == 14 && d == 489)
	//	cout << N[1].salary << " " << t[1] << endl;

	sort(N + 1, N + 1 + n);
	for(int i = 1; i <= n; i++)
	{
		update(t[i], 1);
		//if(n == 14 && d == 489)
		//	cout << t[i] << endl;
		toSalary[N[i].index] = N[i].salary;
	}

	int ans = 0;

	for(int i = 1; i <= n; i++)
	{
		int up = N[i].salary;
		int low = max(0, N[i].salary - d - 1);
		//if(n == 14 && d == 489)
		//	cout << up << " .. " << low << endl;

		ans = max(ans, query(up) - query(low));
		//if(n == 14 && d == 489)
		//	cout << query(up) << "-" << query(low) << endl;
		delIt(N[i].index);
	}

	//if(ans == 0)
	//	cout << n << " " << d << endl;

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
