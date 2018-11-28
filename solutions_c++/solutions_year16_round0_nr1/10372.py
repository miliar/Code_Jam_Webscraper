#include <bits/stdc++.h>	
using namespace std;
int main()
{
	int t, n,i,x,j;
	set <int> seen;

	cin >> t;
	for(j=1;j<=t;j++)
	{
		seen.clear();
		cin >> n;
		if(n)
		{
			x=0;
			while(seen.size()<10)
			{
				x+=n;
				i=x;
				while(i>0)
				{
					seen.insert(i%10);
					i/=10;
				}
			}
			cout << "Case #" << j << ": " << x <<"\n";
		}
		else
			cout << "Case #" << j << ": "<< "INSOMNIA\n";

	}
	return 0;
}