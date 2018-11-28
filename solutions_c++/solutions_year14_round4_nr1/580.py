#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int n, c;
		cin >> n >> c;
		vector<int> v(n);
		for (int i = 0; i < n; i++)
			cin >> v[i];
		sort(v.begin(), v.end());
		int idx1 = 0;
		int idx2 = n - 1;
		int cnt = 0;
		while (idx2 > idx1)
		{
			if (v[idx1] + v[idx2] <= c)
			{
				cnt++;
				idx1++;
				idx2--;
			}
			else
			{
				cnt++;
				idx2--;
			}
		}
		if (idx1 == idx2)
			cnt++;
		cout << cnt << endl;
	}
	return 0;
}
