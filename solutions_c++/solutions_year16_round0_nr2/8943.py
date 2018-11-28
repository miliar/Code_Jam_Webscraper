#include <bits/stdc++.h>
using namespace std;

void solution(string a)
{
	queue<pair<string, int> > fila;
	map<string, int> visitado;
	pair<string, int> aux, T;
	
	string auxi;
	
	int tam = a.size();
	string ans, auxiliar;
	
	for (int i = 0; i < tam; i++) ans += "+";	
	fila.push(make_pair(a, 0));
	while(!fila.empty())
	{
		aux = fila.front();
		fila.pop();
		string u = aux.first;
		
		if(visitado[aux.first] == 0)
		{
			string what = aux.first;
			
			visitado[aux.first] = 1;
			if(aux.first == ans)
			{
				printf("%d\n", aux.second);
				return;
			}
			for (int i = 1; i <= tam; i++)
			{
				auxiliar.clear();
				auxiliar = u.substr(0, i);
				
				auxi.clear();
				
				
				for (int j = i - 1; j >= 0; j--)
				{
						
					if(auxiliar[j] == '+') auxi += "-";
					else auxi += "+";
				}
				auxiliar.clear();
					auxiliar = auxi;	
					auxiliar = auxiliar +  u.substr(i, tam);
					fila.push(make_pair(auxiliar, aux.second + 1));
					
			}
	
	
		}
	}

}


int main()
{
	int n1;
	cin >> n1;
	string a;
	for (int i = 0; i < n1; i++)
	{
		printf("Case #%d: ", i+1);
		cin >> a;
		solution(a);
	}
	
	
	
	return 0;
}
