#include <iostream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	
	int t;
	cin >> t;
	
	for(int k=1; k<=t; k++)
	{
		cout << "Case #" << k << ": ";
		
		int n;
		cin >> n;
		int m[n];
		for(int i=0; i<n; i++)
			cin >> m[i];
			
		int res1 = 0;
		for(int i=1; i<n; i++)
			if(m[i] < m[i-1])
				res1 += m[i-1]-m[i];
		cout << res1 << " ";
		
		int maxDiff = 0;
		for(int i=1; i<n; i++)
			maxDiff = max(m[i-1]-m[i], maxDiff);
			
		int res2 = 0;
		for(int i=0; i<n-1; i++)
			res2 += min(maxDiff, m[i]);
			
		cout << res2 << "\n";
	}

	return 0;
}
