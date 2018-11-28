#include <iostream>

using namespace std;

int main()
{
	int n;
	cin >> n;
	int count = 0;
	int tabela[110][110];
	while(count < n)
	{
		count++;
		bool resp = 1;
		int nLin, nCol;
		cin >> nLin >> nCol;
		for(int i = 0; i < nLin; i++)
			for(int j = 0; j < nCol; j++)
				cin >> tabela[i][j];
		for(int i = 0; i < nLin; i++)
		{
			for(int j = 0; j < nCol; j++)
			{
				int val = tabela[i][j];
				bool valido1 = 1, valido2 = 1;
				for(int k = 0; k < nLin; k++)
				{
					if(tabela[k][j] > val)
						valido1 = 0;
				}
				for(int k = 0; k < nCol; k++)
				{
					if(tabela[i][k] > val)
						valido2 = 0;
				}
				if( !(valido1 || valido2))
					resp = 0;
			}
		}
		cout << "Case #" << count <<": ";
		if(resp == 1)
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}
	return 0;
}
