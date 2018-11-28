#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int Tn;
int a,b,k;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small.out","w",stdout);

	int i,j;

	cin >> Tn;
	for (int T=1;T<=Tn;T++)
	{
		cin >> a >> b >> k;
		int ans = 0;
		for (i=0;i<a;i++)
			for (j=0;j<b;j++)
				if ((i & j) < k)
					ans++;

		cout << "Case #" << T << ": " << ans << endl;

	}
}