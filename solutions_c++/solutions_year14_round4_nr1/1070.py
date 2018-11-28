#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int Tn;
int n, cap;
int a[10010];
bool u[10010];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int i,j;

	cin >> Tn;
	for (int T=1;T<=Tn;T++)
	{
		cin >> n >> cap;
		for (i=0;i<n;i++)
			cin >> a[i];
		sort(a, a+n);
		memset(u, 0, sizeof u);

		int ans = 0;
		for (i=n-1;i>=0;i--)
			if (!u[i])
			{
				u[i] = true;
				ans++;
				int lef = cap - a[i];
				for (j=i-1;j>=0;j--)
					if (!u[j] && a[j]<=lef)
					{
						u[j] = true;
						break;
					}
			}

		cout << "Case #" << T << ": " << ans << endl;

	}
}