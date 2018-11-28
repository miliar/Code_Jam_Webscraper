#include <bits/stdc++.h>

using namespace std;

int main(){
	int n1;
	cin >> n1;
	for (int i = 0; i < n1; i++)
	{
		int cont = 1, sum = 0;
	map<char, int> mapa1;
		string fim;
		int n2;
		int conta = 0, para = 0;
		cin >> n2;
		sum = n2;
		if(n2 != 0) {
		while(1)
		{
			conta++;
			cont++;
			
			stringstream ss;
			ss << sum;
			string soma = ss.str();
	
			int tam = soma.size();
			for (int i = 0; i < tam; i++)
			{
				char c = soma[i];
				mapa1[c]= 1;
					if(mapa1.size() == 10){
						fim = soma;
						para = 1;
						break;
						
						
					}
				
			}
			if(conta > 10000 || para == 1)
			{
				if(conta > 10000) para = 2;
				 break;
				}
				
			sum = n2 * cont;
			
			
		}
		}
		printf("Case #%d: ", i + 1);
		if(para == 2 || n2 == 0) cout << "INSOMNIA" << endl;
		else{
				cout << fim << endl;
		}
	}
	
	return 0;
}


