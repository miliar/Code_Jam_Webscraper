#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int casos, casos2=1;
	double i, j, total, producao, f, x, c, t1, t2;
	
	cin >> casos;
	while(casos--)
	{
		cin >> c >> f >> x;
		producao = 2;
		total = 0;
		
		while(1)
		{
			t1 = x/producao;
			t2 = (c/producao) + x/(producao+f);
			
			
			if(t2 < t1)
			{
				total += (c/producao);
				producao += f;

			}
			else
			{
				total += t1;
				break;
			}

		}
		
		printf("Case #%d: %.7lf\n", casos2++, total);
	}
	
	return 0;
}
