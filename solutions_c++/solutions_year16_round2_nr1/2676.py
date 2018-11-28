#include <fstream>
#include <iostream>
#include "The_Fantastic_Header.h"
using namespace std;

template<typename T>
istream &operator >>(istream &flujo, vector<T> &lista){
	int size = lista.size();
	for (int i = 0; i < size; ++i){
		flujo >> lista[i];
	}
	return flujo;
}

template<typename T>
ostream &operator <<(ostream &flujo, const vector<T> &lista){
	int size = lista.size();
	for (int i = 0; i < size; ++i){
		flujo << lista[i] << " ";
	}
	return flujo;
}

vector<ullint> calcularPrimos(){
	bool primo = true;
	ullint num = 3, square = ullint(sqrt(ULLONG_MAX));
	vector<ullint> v(1, 2);
	while (num <= square){
		ullint i = 0;
		primo = true;
		while (i < v.size() && primo){
			if (num % v[i] == 0){
				primo = false;
			}
			++i;
		}
		if (primo){
			v.push_back(num);
		}
		++num;
	}
	return v;
}

//Poner Comp ord = Comp() implica que en la UVa no compile.
template <typename T, typename Comp = less<T>>
bool busquedaBinaria(const vector<T> &vektor, const T& buscado, int &pos, Comp ord) {
	int ini = 0, fin = vektor.size(), mitad;
	bool encontrado = false;
	// 0 <= ini <= fin <= N
	// array[0..ini) < buscado Y buscado < array[fin..N)
	while (ini < fin && !encontrado) {
		mitad = (ini + fin - 1) / 2; // división entera
		if (ord(buscado, vektor[mitad])) fin = mitad;
		else if (ord(vektor[mitad], buscado)) ini = mitad + 1;
		else encontrado = true;
	}
	if (encontrado) pos = mitad; // en la posición mitad
	else pos = ini; // No encontrado, le corresponde la posición ini (=fin)
	return encontrado;
}

//Poner Comp ord = Comp() implica que en la UVa no compile.
template <typename T, typename Comp = less<T>>
void colocarInsercion(vector<T> & lista, int i, Comp ord) {
	T elemento = lista[i];
	int j = i;
	while (j > 0 && ord(elemento, lista[j - 1])) {
		lista[j] = lista[j - 1];
		--j;
	}
	if (j != i) lista[j] = elemento;
}

//Poner Comp ord = Comp() implica que en la UVa no compile.
template <typename T, typename Comp = less<T>>
void ordenarInsercion(vector<T> & lista, Comp ord ) {
	int N = lista.size();
	for (int i = 1; i < N; ++i) {
		colocarInsercion(lista, i, ord);
	}
}
