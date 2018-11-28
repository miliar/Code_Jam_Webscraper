#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int Tn;
int n;
int a[1010];

int up[1010];
int down[1010];

int calcup(int x)
{
	int res = 0;
	for (int i=1;i<x;i++)
		if (a[i] > a[x])
			res++;
	return res;
}
int calcdown(int x)
{
	int res = 0;
	for (int i=n;i>x;i--)
		if (a[i] > a[x])
			res++;
	return res;
}

int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("B-small.out","w",stdout);

	int i,j;

	cin >> Tn;
	for (int T=1;T<=Tn;T++)
	{
		cin >> n;
		for (i=1;i<=n;i++)
			cin >> a[i];
		memset(up, 0, sizeof up);
		memset(down, 0, sizeof down);

		for (i=1;i<=n;i++)
			up[i] = up[i-1] + calcup(i);
		for (i=n;i>0;i--)
			down[i] = down[i+1] + calcdown(i);
		int ans = 2147483647;
		for (i=0;i<=n;i++)
			ans = min(ans, up[i]+down[i+1]);

		cout << "Case #" << T << ": " << ans << endl;

	}
}