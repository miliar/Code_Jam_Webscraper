#include <iostream>
#include <math.h>

using namespace std;

main()
{
	unsigned long long int T,cont;
	unsigned long long int areai, area,t,tinta,r, nova,n,aux,a2,a1,circ,total;
	cin >> T;
	for(int i=1; i<=T; i++)
	{
		cin >> r >> t;
		aux = r+1;
		circ = 0;
		total = 0;
		while(1)
		{
			a1 = (r*r);
			a2 = (aux*aux);
			total += (a2-a1);
			if(total > t) break;
			else
			{
				circ++;
				r = r + 2;
				aux = r+1;
			}
		}
		cout << "Case #" << i << ": " << circ << endl; 
	}
	return 0;
}
