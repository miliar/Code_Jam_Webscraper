#include <iostream>
using namespace std;
const int maxn = 1005;
int d[maxn]; 

int main()
{
	int T, count = 0, n; 
	int up, i, ans, sum; 

	cin >> T; 
	while(T--){
		cin >> n; 
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
		count++;
		printf ("Case #%d: %d\n", count, ans); 
	}
}