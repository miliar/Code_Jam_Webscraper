#include <bits/stdc++.h>

using namespace std;

int S,Total=0,Paradas=0,arreglo[1001],resultados[101],T;
char arreglochar[1001];

int main()
	{
		cin>>T;
		for(int j=1;j<=T;j++)
			{
				cin>>S;
				for(int i=0;i<=S;i++)
					{
						cin>>arreglochar[i];
						arreglo[i]=(int)arreglochar[i]-48;
					}
				Paradas=arreglo[0];
				
				for(int Pib=0;Pib<=S;Pib++)
					{
						if (arreglo[Pib+1]!=0)
							{
								if (Pib+1>Paradas)
									{
										Total+=Pib+1-Paradas;
										Paradas+=Pib+1-Paradas;
										Paradas+=arreglo[Pib+1];
									}
								else
									Paradas+=arreglo[Pib+1];
							}
					}
					
				resultados[j]=Total;
				Total=0;
				Paradas=0;
			}
			
		for(int z=1;z<=T;z++)
			{
				cout<<"Case #"<<z<<": "<<resultados[z]<<endl;
			}
		
		return 0;
	}
