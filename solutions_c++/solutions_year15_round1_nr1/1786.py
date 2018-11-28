#pragma error(disable:4996)
#include<iostream>
#include<iomanip>
#include<cstring>
#include<string>
#include<algorithm>
#include<map>
#include<set>
#include<vector>
#include<queue>
using namespace std;
typedef long long LL;
const LL MAXSIZE = 10000000;
int a[1000000];
LL L;


int main()
{
	errno_t err1;
	errno_t err2;
	FILE *fin, *fout;
	err1 = freopen_s(&fin, "A-large.in", "r", stdin);
	//err1 = freopen_s(&fin, "A-small-attempt0 (1).in", "r", stdin);
	err2 = freopen_s(&fout, "out.txt", "w", stdout);
	LL T;
	cin >> T;
	memset(a, 0, sizeof(a));
	for (LL z = 1; z <= T; ++z)
	{
		int n;
		cout << "Case #" << z << ": ";
		cin >> n;
		for (int i = 0; i < n; ++i)
			cin >> a[i];
		int ans = 0;
		int ub = 0;
		for (int i = 1; i < n; ++i)
		{
			
			if (a[i] < a[i - 1])
			{
				ans += a[i-1] - a[i];
				if (a[i-1] - a[i]>ub)
					ub = a[i-1] - a[i];
			}
		}
		int ans2 = 0;
		for (int i = 0; i < n-1; ++i)
		{
			if (a[i] < ub)
				ans2 += a[i];
			else ans2 += ub;
		}
		cout << ans << " "<<ans2<<endl;
	}

}
