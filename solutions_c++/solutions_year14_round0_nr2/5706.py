#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	int k,i;
	cin >> k;
	for(i=1;i<=k;i++)
	{
		double c,producao=2,f,x,total=0;
		double csf,ccf;
		cin >> c >> f >> x;
		

		csf = x/producao;
		ccf = c/producao;
	
		while ((ccf + (x/(producao+f))) < csf)
		{
			total+=ccf;
			producao+=f;
			csf = x/producao;
			ccf = c/producao;
		}
		total+=csf;
		cout << "Case #" << i << ": ";
		printf("%.7lf\n",total); 
		
	}
	return 0;
}
