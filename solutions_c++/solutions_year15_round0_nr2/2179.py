#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <cmath>
#include <deque>
using namespace std;

#define FROM_FILE

void prepare()
{
	ios_base::sync_with_stdio(0);
#ifdef FROM_FILE
	freopen("E:\\in.txt", "r", stdin);
	freopen("E:\\out.txt", "w", stdout);
#endif
}

int Solve(int num, int koz)
{

	return ((num / koz) + (num % koz ? 0 : -1));
}

int main()
{

	prepare();

	int t;
	cin >> t;
	for(int doubleT = 0; doubleT < t; doubleT++)
	{
		int n;
		cin >> n;
		vector<int> a(n);
		for(int i = 0; i < n; i++)
		{
			cin >> a[i];
		}

		int res = 1000 * 1000 * 1000;
		for(int maxp = 1; maxp < 1003; maxp ++)
		{
			int lcREZ = maxp;
			for(int i = 0; i < n; i++)
			{
				lcREZ += Solve(a[i] , maxp);
			}
			res = min(res, lcREZ);
		}

		printf("Case #%d: %d\n", doubleT+1, res);
	}


	return 0;
}





