#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;

int main()

{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T,L, niv[1001], cont, ova, k, i, j, n;
	char number[1001]; 
	
	cin>>T;	
	
	for( int i = 1; i<=T; i++)
	{
	
		cin>>n>>number;
		
		for (int j=0; j<=n;j++)
		{
			switch (number[j])
			{
				case '0': niv[j]=0; break;
				case '1': niv[j]=1; break;
				case '2': niv[j]=2; break;
				case '3': niv[j]=3; break;
				case '4': niv[j]=4; break;
				case '5': niv[j]=5; break;
				case '6': niv[j]=6; break;
				case '7': niv[j]=7; break;
				case '8': niv[j]=8; break;
				case '9': niv[j]=9; break;
			}
		}
		

		
		cont=niv[0];
		ova=0;
		
		for (int k=1; k<=n;k++)
		{
			if (niv[k] != 0)
			{
				while (cont<k)
				{
					cont = cont +1;
					ova = ova +1;
				}
			}
			cont = cont + niv[k];
		}
		
		cout<<"Case #"<<i<<": "<<ova<<endl;	
	}	
	
	return 0;
}
