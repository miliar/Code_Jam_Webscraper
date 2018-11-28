#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin >> t;
	int caso=1;
	while(t--){
		string entrada;
		cin >> entrada;
		string saida="";
		saida+=entrada[0];
		for (int i = 1; i < entrada.size(); i++)
		{
			if(entrada[i] >= saida[0]) saida.insert(saida.begin(), entrada[i]);
			else saida+=entrada[i];
		}
		printf("Case #%d: %s\n", caso++, saida.c_str());
		
	}

	return 0;
}
