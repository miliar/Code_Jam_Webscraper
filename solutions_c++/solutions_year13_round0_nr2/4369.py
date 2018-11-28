#include <iostream>
#include <vector>

using namespace std;

void recortar(vector<vector<int> > &cortado, int mode, int num, int h);
bool sonIguales(vector<vector<int> > &entrada, vector<vector<int> > &cortado);

int main(){
	
	unsigned long long T, k=1;
	cin >> T;
	
	while (k<=T){
		
		int n, m, aux;
		
		cin >> n >> m;
		
		vector<int> maxFilas(n,0), maxCols(m,0);
		vector<vector<int> > entrada, cortado;
		
		entrada.resize(n);
		cortado.resize(n);
		
		for (int i = 0; i < n; i++)
		{
			entrada[i].resize(m);
			cortado[i].resize(m);
			
			for (int j = 0; j < m; j++)
			{
				cin >> aux;
				if (aux > maxFilas[i])
					maxFilas[i] = aux;
					
				if (aux > maxCols[j])
					maxCols[j] = aux;
				
				entrada[i][j] = aux;
				cortado[i][j] = 100;
			}
			
		}
		
		for (int i = 0; i < n; i++)
		{
			recortar(cortado, 0, i, maxFilas[i]);
		}
		
		for (int i = 0; i < m; i++)
		{
			recortar(cortado, 1, i, maxCols[i]);
		}
		
		
		cout << "Case #" << k << ": ";
		if (sonIguales(entrada, cortado) ){
			cout << "YES";
		} else{
			cout << "NO";
		}
		cout << endl;
		++k;
	}
	
	return 0;
}

void recortar(vector<vector<int> > &cortado, int mode, int num, int h){
	if (mode==0){
		for (int i = 0; i < (int)cortado[0].size(); i++)
		{
			if (h < cortado[num][i])
				cortado[num][i] = h;
		}
		
	} else{
		for (int i = 0; i < (int)cortado.size(); i++)
		{
			if (h < cortado[i][num])
				cortado[i][num] = h;
		}
	}
}

bool sonIguales(vector<vector<int> > &entrada, vector<vector<int> > &cortado){
	for (int i = 0; i < (int)entrada.size(); i++)
	{
		for (int j = 0; j < (int)entrada[0].size(); j++)
		{
			if (entrada[i][j] != cortado[i][j]) return false;
		}
		
	}
	return true;
}
