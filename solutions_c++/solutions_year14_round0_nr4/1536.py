#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, n, caseno = 1;
	cin >> t;
	while(t--)
	{
		cin >> n;
		double naomi[n], ken[n];
		for(int i=0; i<n; i++)
			cin >> naomi[i];
		for(int i=0; i<n; i++)
			cin >> ken[i];
		sort(naomi, naomi+n);
		sort(ken, ken+n);

		int dec = 0, war = 0, naomiidx = 0, kenidx = 0;
		while(kenidx < n)
		{
			if(naomi[naomiidx] < ken[kenidx])
			{
				naomiidx++;
				kenidx++;
			}
			else
				kenidx++;
		}
		war = n - naomiidx;

		naomiidx = n-1; 
		kenidx = n-1;

		while(kenidx >= 0)
		{
			if(naomi[naomiidx] > ken[kenidx])
			{
				naomiidx--;
				kenidx--;
				dec++;
			}
			else
				kenidx--;
		}
		cout << "Case #" << caseno << ": " << dec << " " << war << endl;
		caseno++;
	}
	return 0;
}