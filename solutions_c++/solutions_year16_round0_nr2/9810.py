#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;

int main(){
	optimizar_io
	int casos;
	cin >> casos;
	for(int ind = 1; ind <= casos; ind++){
		cout << "Case #" << ind << ": ";

		string cadena;
		cin >> cadena;

		int res = 0;
		for(int i = 1; i < cadena.size(); i++)
			if(cadena[i] != cadena[i - 1] ) res++;

		if(cadena[cadena.size() - 1] == '-' ) res++;
		cout << res << "\n";
	}

}
