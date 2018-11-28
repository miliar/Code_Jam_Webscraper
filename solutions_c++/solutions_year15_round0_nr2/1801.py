#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <unordered_map>
#include <utility>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
using namespace std;
const int maxn = 1005;
int d[maxn]; 

int main()
{
	int T, I, n; 
	int up, i, ans, sum; 

	scanf ("%d", &T); 
	for (I=1; I<=T; I++)
	{
		scanf ("%d", &n); 
		ans = 0; 
		for (i=0; i<n; i++)
		{
			scanf ("%d", d+i); 
			ans = max(ans, d[i]); 
		} 

		for (up = 1; ; up++)
		{
			sum = 0; 
			for (i=0; i<n; i++)
			{
				sum += (d[i] + up - 1) / up - 1; 
			}
			
			ans = min(ans, sum + up); 
			//printf ("%d %d %d\n", up, sum, sum + up); 

			if (sum == 0) break; 
		}
		printf ("Case #%d: %d\n", I, ans); 
	}
}