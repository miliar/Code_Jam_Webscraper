#include<iostream>
#include<fstream>
#include<vector>

using namespace std;


bool ya(const bool esta[10]){
	return esta[0] && esta[1] && esta[2] && esta[3] && esta[4] && esta[5]
		&& esta[6] && esta[7] && esta[8] && esta[9];
}

void descomponer(int n, bool cifras[10]){
	int mem = n;
	int div = 10;
	bool prim = true;
	while (mem!=0 || prim){
		cifras[mem%div] = true;
		mem /= div;
		prim = false;
	}
}

int main(){
	int casos;
	int n;
	/*ofstream arch;
	ifstream ent;
	ent.open("entrada.txt");
	arch.open("salida.txt");*/
	int mem;
	int mult;
	cin >> casos;
	bool esta[10];
	for (int ctrl = 0; ctrl < casos; ctrl++){
		for (int i = 0; i < 10; i++)esta[i] = false;
		mult = 1;
		cin >> n;
		mem = n;
		if (n == 0)cout << "Case #" << ctrl+1 << ": INSOMNIA\n";
		else{
			while (!ya(esta)){
				descomponer(n, esta);
				mult++;
				n = mem*mult;
			}
			mult--;
			n = mem*mult;
			cout << "Case #" << ctrl+1 << ": "<<n<<'\n';
		}
	}
}