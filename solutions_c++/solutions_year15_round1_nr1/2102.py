#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <unordered_map>
#include <utility>
#include <cmath>
using namespace std;
const int maxn = 1005; 
int a[maxn]; 

int main()
{
	int T, n, I, ans, i; 
	scanf ("%d", &T); 
	for (I=1; I<=T; I++)
	{
		scanf ("%d", &n); 
		for (i=0; i<n; i++) scanf ("%d", a+i); 
		printf ("Case #%d: ", I); 
		ans = 0; 
		for (i=1; i<n; i++)
		{
			if (a[i-1] > a[i]) ans += a[i-1] - a[i]; 
		}
		printf ("%d ", ans); 

		int Max = 0; 
		for (i=1; i<n; i++)
			Max = max(Max, a[i-1]-a[i]); 
		ans = 0; 
		for (i=0; i<n-1; i++)
		{
			ans += min(Max, a[i]); 
		}
		printf ("%d\n", ans); 
	}
}