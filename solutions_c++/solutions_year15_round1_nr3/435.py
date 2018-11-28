		//	   - -- --- ---- -----be name khoda----- ---- --- -- -		\\

#include <bits/stdc++.h>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
typedef long long ll;
#define min(A, B) ((A) < (B) ? (A) : (B))
const int N = 5005;

struct Point{
	ll x, y;
};

Point a[N];

inline ll cross(Point A, Point B) { return A.x * B.y - A.y * B.x; }
inline Point ve(Point A, Point B) { return Point{A.x - B.x, A.y - B.y}; }

int main()
{
	int _ = in();
	for(int i = 1; i <= _; i++)
	{
		printf("Case #%d:\n", i);
		int n = in();
		for(int i = 0; i < n; i++)
			a[i] = Point{in(), in()};
		for(int i = 0; i < n; i++)
		{
			int best = n - 1;
			for(int j = 0; j < n; j++)
			{
				if(j == i)
					continue;
				int cnt1 = 0;
				int cnt2 = 0;
				for(int k = 0; k < n; k++)
				{
					ll x = cross(ve(a[i], a[j]), ve(a[i], a[k]));
					if(x < 0)
						cnt1++;
					if(x > 0)
						cnt2++;
				}
				best = min(best, min(cnt1, cnt2));
			}
			cout << best << "\n";
		}
	}
}
