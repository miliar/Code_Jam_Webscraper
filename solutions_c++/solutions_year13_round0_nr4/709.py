#include <iostream>
using namespace std;
int test; int n; int k; int kk[30]; int g = 0;
bool st[9000000];
bool c[30];
int nk[300];
int ct[300];
int ck[30][40];
int way[9000000][20];
int now[20];
int all = 0;
int d[24];
void push(int stan)
{
	
	if (st[stan])
	{
		int less = 0;
		for (int i = 1; i <= all; i++)
		{
			if (way[stan][i] < now[i])
			{
				less = 1;
				break;
			}
			if (way[stan][i] > now[i])
			{
				less = 2;
				break;
			}
		}
		if (less != 2)
			return;
	}
	st[stan] = true;
	for (int i = 1; i <= all; i++)
		way[stan][i] = now[i];
	for (int i = 1; i <= n; i++)
		if (!c[i] && nk[ct[i]])
		{
			c[i] = true;
			for (int j = 1; j <= ck[i][0]; j++)
				nk[ck[i][j]]++;
			nk[ct[i]]--;
			all++;
			now[all] = i;
			push(stan + d[i]);
			now[all] = 0;
			all--;
			nk[ct[i]]++;
			for (int j = 1; j <= ck[i][0]; j++)
				nk[ck[i][j]]--;
			c[i] = false;
		}
}

int main()
{
	d[0] = 1;
	for (int i = 1; i <= 22; i++)
		d[i] = d[i - 1] * 2;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	cin >> test;

	for (int t = 1; t <= test; t++)
	{
		
		for (int i = 0; i <= d[22]; i++) st[i] = false;
		for (int i = 1; i <= 30; i++) c[i] =false;
		for (int i = 0; i <= 200; i++) nk[i] = 0;
		for (int i = 0; i <= d[22]; i++)
			for (int j = 0; j < 22; j++)
				way[i][j] = 10000;
	    all = 0;
		cout << "Case #" << t << ": ";
		cin >> k >> n;
		int x;
		for (int i = 1; i <= k; i++)
		{
			cin >> x;
			nk[x]++;
		}
		for (int i = 1; i <= n; i++)
		{
			cin >> ct[i] >> ck[i][0];
			for (int j = 1; j <= ck[i][0]; j++)
				cin >> ck[i][j];
		}
		for (int i = 1; i <= d[22]; i++)
			st[i] = false;
		for (int i = 1; i <= d[22]; i++)
			for (int j = 1; j <= 22; j++)
				way[i][j] = 100;
		all = 0; push(0);
		if (st[d[n + 1] - 2])
			for (int i = 1; i <= n; i++)
			{
				cout << way[d[n + 1] - 2][i];
				if (i < n) cout << " ";
				if (i == n) cout << endl;
			}
		else
			cout << "IMPOSSIBLE" << endl;
	}
}