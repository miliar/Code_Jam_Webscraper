#include <bits/stdc++.h>

using namespace std;

double c, f, x;

int main()
{
	int nCasos;
	cin>>nCasos;
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		cin>>c>>f>>x;
		
		double k = 2;
		double best = x / k;
		double cur = 0;
		
		while(c < x && c / k + x / (k + f) < x / k)
		{
			cur = cur + c / k;
			best = min(best, cur + x / (k + f));
			k += f;
		}

		printf("Case #%d: %.10lf", caso, best);
		
		cout<<endl;
	}
	
	return 0;
}
