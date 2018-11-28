#include <iostream>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 10010;

int n, s, a[MAXN];
int qh, q[MAXN];

int Work()
{
	cin >> n >> s;
	for (int i = 0; i < n; i ++)
		cin >> a[i];
	sort(a, a + n);
	int ret = 0;
	qh = 0; 
	for (int i = n - 1; i >= 0; i --)
	{
		if (qh > 0 && q[qh-1] >= a[i]) 
			qh --;
		else 
		{
			q[qh++] = s - a[i];
			ret ++;
		}
	}
	return ret;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin.sync_with_stdio(false);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt ++)
		cout << "Case #" << tt << ": " << Work() << endl;
	return 0;
}