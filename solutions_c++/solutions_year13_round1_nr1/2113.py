#include<iostream>
#include<math.h>

using namespace std;

int main()
{
	int casos, contador=1, circ;
	int r, t, aux;
	double a1, a2, tamanho, total;

	cin >> casos;
	while(casos--)
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
			if(total > t)
				break;
			else
			{
				circ++;		
				r = r + 2;
				aux = r+1;
			}
		}
		cout << "Case #" << contador << ": " << circ << endl;
		contador++;
	}
return 0;
}







			


			
