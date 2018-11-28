#include <iostream>
#include <cstdio>
#include <list>
#include <vector>

using namespace std;

struct cuadradito
{
    int y;
    int x;
    int altura;
};

bool mayor(cuadradito A, cuadradito B) {
	return A.altura > B.altura;
}

int main() {
	#ifdef BBB
		freopen("ej1.in", "r", stdin);
	#endif
	int casos;
	cin >> casos;
	for(int asd = 1; asd<=casos; asd++) {
		int largo, ancho;
		cin >> largo >> ancho;
		vector<int> losLargos (largo, 0);
		vector<int> losAnchos (ancho, 0);
		list<cuadradito> lista;
		for(int i=0; i<largo; i++) {
			for(int k=0; k<ancho; k++) {
				cuadradito nuevo;
				nuevo.x = k;
				nuevo.y = i;
				cin >> nuevo.altura;
				lista.push_back(nuevo);
			}
		}
		lista.sort(mayor);
		list<cuadradito>::iterator it;
		bool anda = true;
		for (it=lista.begin(); it!=lista.end(); ++it) {
			if( losLargos[(*it).y] > (*it).altura & losAnchos[(*it).x] > (*it).altura ) {
				anda = false;
				break;
			} else {
				losLargos[(*it).y] = max(losLargos[(*it).y], (*it).altura);
				losAnchos[(*it).x] = max(losAnchos[(*it).x], (*it).altura);
			}
		}
		cout << "Case #" << asd << ": "; 
		if (anda) {
			cout << "YES";
		} else {
			cout << "NO";
		}
		cout << endl;
		/*
		list<cuadradito>::iterator it;
		for (it=lista.begin(); it!=lista.end(); ++it)
   			cout << ' ' << (*it).altura << '(' << (*it).x << ',' << (*it).y << ')';
  		cout << '\n';
		cout << endl;*/
	}	
}