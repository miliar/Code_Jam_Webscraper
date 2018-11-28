#include <iostream>

using namespace std;

int main()
{	
	int x,y,z,h,i,k,t,iterador;
	cin >> t;
	for(iterador=1;iterador<=t;iterador++)
	{
		int cont=0;
		cin >> x >> y >> h;
		for(i=0;i<x;i++)
		{
			for(k=0;k<y;k++)
			{
				z = i&k;
				if(z < h)
					cont++;
			}
		}
		cout << "Case #" << iterador << ": " << cont << endl;
	}
	return 0;
}
