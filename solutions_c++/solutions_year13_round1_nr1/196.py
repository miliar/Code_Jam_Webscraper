#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		double r, t;
		cin>>r>>t;
		
		double lo = 1, hi = t;
		for(int i=0; i<100; i++)
		{
			double mid = (lo + hi) / 2;
			if(mid * (2.0 * r + 2.0 * mid - 1.0) < t) lo = mid;
			else hi = mid;
		}
		
		unsigned long long x = lo + 1.5;
		while(x * (2 * r + 2 * x - 1) > t) x--;
		
		cout<<"Case #"<<caso<<": "<<x<<endl;
	}
	
	return 0;
}
