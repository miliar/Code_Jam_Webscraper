#if 1
#include <iostream>
#include <cstdio>
#include <sstream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <string>
#include <numeric>
#include <cstring>
#include <ctime>


using namespace std;
#define mp make_pair
#define X first
#define Y second
#define pb push_back

typedef pair<int, int> pii ;
typedef long long LL;
typedef long double LD;
typedef vector<int> vi;

const LL inf = 1e9;
const LD eps = 1e-9;

int main()        
{
    freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int q = 0; q < T; q++)
	{
		int n, s;
		scanf("%d %d", &n, &s);
		vector <int> a(n);
		for (int i = 0; i < n; i++)
		{
			scanf("%d", &a[i]);
		}
		sort(a.rbegin(), a.rend());
		vector <char> used(n, 0);
		int cnt = 0;
		for (int i = 0; i < n; i++)
		{
			if (!used[i])
			{
				used[i] = 1;
				cnt++;
				for (int k = i + 1; k < n; k++)
				{
					if (a[i] + a[k] <= s && !used[k])
					{
						used[k] = 1;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n", q + 1, cnt);
	}
    return 0;
}
#endif