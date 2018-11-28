/* bhupkas */

#include "bits/stdc++.h"

using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int tc = 1 ; tc <= t ; ++tc)
	{
		printf("Case #%d: ",tc);
		int a,b,k;
		cin >> a >> b >> k;
		int re = 0;
		for(int i = 0 ; i < a ; ++i)
			for(int j = 0 ; j < b ; ++j)
			{
				if((i&j) < k)	re++;
				//cout << (i&j) << endl;
			}
				
		cout << re << endl;
	}
	return 0;
}