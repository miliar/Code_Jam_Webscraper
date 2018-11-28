#pragma warning(disable:4996)
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<cmath>
#include<cstdio>
#include<set>
#define maxn 1500
using namespace std;

double a[maxn];
double b[maxn];
int n;

int main()
{
	freopen("D-large.in.txt", "r", stdin);
	freopen("D-large.out.txt", "w", stdout);
	int T; cin >> T; int ca = 0;
	while (T--)
	{
		//set<double> sa;
		//set<double> sb;
		scanf("%d", &n);
		for (int i = 0; i < n; i++){
			scanf("%lf", a + i);
		}
		for (int i = 0; i < n; i++){
			scanf("%lf", b + i);
		}
		sort(a, a + n);
		sort(b, b + n);
		int ans1 = 0, ans2 = 0;
		int stidx = 0;
		for (int i = 0; i < n; i++){
			stidx = upper_bound(a + stidx, a + n, b[i]) - a;
			if (stidx == n) break;
			else ans1++;
			stidx++;
		}
		int l = 0, r = n - 1;
		for (int i = n - 1; i >= 0; i--){
			if (a[i]>b[r]) {
				l++; ans2++;
			}
			else{
				r--;
			}
		}
		printf("Case #%d: %d %d\n", ++ca, ans1, ans2);
	}
	return 0;
}