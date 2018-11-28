#include <fstream>
#include <bitset>
#include <string>
#include <vector>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <stack>

using namespace std;

typedef unsigned long long int ullint;
const int STR_SIZE = 32;
const int CASOS = 500;
const ullint DOS_A_LA_30 = 1073741824;
const ullint DOS_A_LA_31 = 2147483648;
//const long int TAM_BITSET = 1000000;
const vector<int> solucion = { 3, 2, 5, 2, 7, 2, 3, 2, 11 };

struct number{
	string nombre;
	vector<int> lista = solucion;
};

vector<number> create();
string cambiar(ullint n);
/*
bool mod(const bitset<TAM_BITSET> &primos, string n, ullint &m);
void primos(bitset<TAM_BITSET> &primos);
bool divis(const bitset<TAM_BITSET> &primos, ullint &n);
void primo(bitset<TAM_BITSET> &primos);*/
bool noPrimo(number &n);
bool parUnos(const string &palabra);
bool div3(const string &palabra);
bool div11(const string &palabra);

int main(){
	vector<number> tabla;
	ifstream entrada("entrada.txt");
	ofstream salida("salida.txt");
	tabla = create();
	salida << "Case #1:\n";
	int size = tabla.size();
	for (int i = 0; i < CASOS ; ++i){
		salida << tabla[i].nombre;
		for (int j = 0; j < 9; ++j){
			salida << " " << tabla[i].lista[j];
		}
		salida << "\n";
	}
	return 0;
}

vector<number> create(){
	int aux, size = 0;
	vector<number> create;
	//bitset<TAM_BITSET> primos;
	//primo(primos);
	for (int i = 2; i < DOS_A_LA_30 && size < CASOS; ++i){
		number change;
		aux = DOS_A_LA_31 + 2 * i + 1;
		change.nombre = cambiar(aux);
		change.lista = solucion;
		if (noPrimo(/*primos*/ change)){
			create.push_back(change);
			++size;
		}
	}
	return create;
}
bool parUnos(const string &palabra){
	bool ok = true;
	for (int i = 0; i < palabra.size(); ++i){
		if (palabra[i] == '1'){
			ok = !ok;
		}
	}
	return ok;
}
bool div3(const string &palabra){
	int suma = 0;
	for (int i = 0; i < palabra.size(); ++i){
		if (palabra[i] == '1' && i % 2 == 0){
			++suma;
		}
		else if (palabra[i] == '1'){
			suma += 2;
		}
	}
	return ((suma % 3) == 0);
}
bool div7mod6(const string &palabra){
	int suma = 0;
	for (int i = 0; i < palabra.size(); ++i){
		if (palabra[i] == '1' && i % 2 == 0){
			++suma;
		}
		else if (palabra[i] == '1'){
			--suma;
		}
	}
	return (suma % 7) == 0;
}
bool div11(const string &palabra){
	int sumai = 0, sumad = 0;
	for (int i = 0; i < palabra.size(); i = i + 2){
		if (palabra[i] == '1'){
			++sumai;
		}
		if (i + 1 < palabra.size() && palabra[i + 1] == '1'){
			++sumad;
		}
	}
	return ((max(sumai, sumad) - min(sumai, sumad)) % 11 == 0);
}
string cambiar(ullint n){
	int aux = n;
	string ans = "";
	stack<char> pila;
	for (int i = 0; i < STR_SIZE; ++i){
		aux = n % 2;
		pila.push(char(aux + int('0')));
		n = n / 2;
	}
	while (!pila.empty()){
		ans += pila.top();
		pila.pop();
	}
	return ans;
}
bool noPrimo(number &n){
	bool ok = true;
	ullint aux = 6;
	ok = (parUnos(n.nombre) && div3(n.nombre) && div11(n.nombre) && div7mod6(n.nombre));
	return ok;
}
/*
bool mod(const bitset<TAM_BITSET> &primos, string n, ullint &m){
	ullint aux = 0, num = 1;
	for (int i = n.size() - 1; i >= 0; --i){
		aux += (int(n[i] - '0'))*num;
		num *= m;
	}
	m = aux;
	return (divis(primos, m) && m != aux);
}
bool divis(const bitset<TAM_BITSET> &primos, ullint &n){
	bool ok = false;
	for (int i = 0; i < primos.size() && !ok; ++i){
		ok = (primos[i] && n % (i + 2) == 0);
		if (ok){
			n = i + 2;
		}
	}
	return ok;
}
void primo(bitset<TAM_BITSET> &primos){
	primos.set();
	for (int i = 2; i < 100; ++i){
		if (primos[i - 2]){
			for (int j = 2; j < 100; ++j){
				primos[i*j - 2] = false;
			}
		}
	}
}*/