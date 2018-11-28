#include<iostream>

using namespace std;

int main()
{
	int v[17], i, j, casos, x, n2, pos, linha, contador=1;
	
	cin >> casos;
	while(casos--)
	{
		cin >> linha;
		
		for(i=0; i<17; i++)
			v[i] = 0;
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				cin >> x;

				if(linha == i+1)
				{
					v[x]++;

				}
			}
		}

		cin >> linha;
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				cin >> x;
				if(linha == i+1)
				{
					v[x]++;
				}
			}
		}
		
		n2 = 0;
		pos = 0;
		for(i=0; i<17; i++)
		{
			if(v[i] == 2)
			{
				n2++;
				pos = i;
			}
		}
		
		cout << "Case #" << contador++ << ": ";
		if(n2 >= 2)
			cout << "Bad magician!" << endl;
		else if(n2 == 1)
			cout << pos << endl;
		else
			cout << "Volunteer cheated!" << endl;	
	}
	
	return 0;
}
					
					
