#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#define MAXN 1010
using namespace std;

int Tn;
int n;
double a1[MAXN], a2[MAXN];
bool u1[MAXN], u2[MAXN];

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);

	int i,j;

	cin >> Tn;
	for (int T=1;T<=Tn;T++)
	{
		int ans1=0, ans2=0;
		cin >> n;
		for (i=0;i<n;i++)
			cin >> a1[i];
		for (i=0;i<n;i++)
			cin >> a2[i];
		sort(a1,a1+n);
		sort(a2,a2+n);
		memset(u1, 0, sizeof u1);
		memset(u2, 0, sizeof u2);

		for (i=0;i<n;i++)
		{
			for (j=0;j<n && a2[j]<a1[i];j++)
				if (!u2[j])
				{
					ans1++;
					u2[j] = true;
					break;
				}
		}
		for (i=0;i<n;i++)
			for (j=0;j<n && a1[j]<a2[i];j++)
				if (!u1[j])
				{
					ans2++;
					u1[j] = true;
					break;
				}

		printf("Case #%d: %d %d\n", T, ans1, n-ans2);
	}
}