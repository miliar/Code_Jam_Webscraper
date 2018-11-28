#include <iostream>
#include <fstream>

using namespace std;
int main(int argc, char const *argv[])
{
	int personas[101];
	int contv = 0;
	int contn = 0;
	int total = 0;
	int veces;
	int vecesn;
	int aux;
	string valores;

	cin >> veces;
	while(contv < veces)
	{
		personas[contv] = 0;
		cin >> vecesn;
		cin >> valores;
		while(contn < vecesn+1)
		{
			
			if(valores[contn] == '0')
			{
				contn++;
				continue;
			}
			else if(contn > total)
			{
				aux = contn - total;
				total += aux;
				personas[contv] += aux;
			}
			total += valores[contn] - '0';
			contn++;
		}
		cin.ignore();
		contv++;
		contn=0;
		total=0;
	}

	ofstream result("result A.out"); 
	for (int i = 0; i < contv; i++)
	{
		result << "Case #" << i+1 << ": " << personas[i] << endl;
	}

	result.close();
	return 0;
}