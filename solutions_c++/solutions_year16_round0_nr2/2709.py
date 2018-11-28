#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <bitset>
#include <stack>
using namespace std;

const int TAM_BITSET = 100;

int create(bitset<TAM_BITSET> &pastel, const string &aux);
bool allInSize(const bitset<TAM_BITSET> &pastel, int size);
void flipTrue(bitset<TAM_BITSET> &pastel, int size, int &movs);
void flipFalse(bitset<TAM_BITSET> &pastel, int size, int &movs);

int main(){
	ifstream entrada("entrada.txt");
	ofstream salida("salida.txt");
	int casos;
	entrada >> casos;
	for (int i = 0; i < casos; ++i){
		string aux;
		entrada >> aux;
		bitset<TAM_BITSET> pastel;
		int size = create(pastel, aux);
		int movs = 0;
		while (!allInSize(pastel, size)){
			if (pastel[0]){
				flipTrue(pastel, size, movs);
			}
			else flipFalse(pastel, size, movs);
		}
		salida << "Case #" << i + 1 << ": " << movs << "\n";
	}
	return 0;
}

int create(bitset<TAM_BITSET> &pastel, const string &aux){
	int n = aux.size();
	for (int i = 0; i < n; ++i){
		if (aux[i] == '+'){
			pastel[i] = true;
		}
		else{
			pastel[i] = false;
		}
	}
	return n;
}
bool allInSize(const bitset<TAM_BITSET> &pastel, int size){
	bool ok = true;
	for (int i = 0; i < size && ok; ++i){
		ok = pastel[i];
	}
	return ok;
}
void flipTrue(bitset<TAM_BITSET> &pastel, int size, int &movs){
	int i = 0;
	while (i < size && pastel[i]){
		++i;
	}
	while (i < size && !pastel[i]){
		pastel[i] = true;
		++i;
	}
	movs += 2;
}
void flipFalse(bitset<TAM_BITSET> &pastel, int size, int &movs){
	int i = 0;
	while (i < size && !pastel[i]){
		pastel[i] = true;
		++i;
	}
	++movs;
}