#include <fstream>

using namespace std;

const short int TAM = 10;

typedef unsigned long long int lint;

void resol(int i, ifstream & in, ofstream & out);

int main(){
	ifstream in; ofstream out;
	in.open("A-large.in");
	out.open("A-large.out");
	int nCase;
	in >> nCase;
	for (int i = 0; i < nCase; ++i)
		resol(i, in, out);	
	in.close();
	out.close();
	return 0;
}

void resol(int i, ifstream & in, ofstream & out){
	lint num;
	in >> num;
	out << "Case #" << i + 1 << ": ";
	if (num == 0) out << "INSOMNIA" << '\n';
	else{
		bool vector[TAM], ok = false;
		lint aux, num2, pos, cont = 1;
		for (int j = 0; j < TAM; ++j) vector[j] = false;

		while (!ok){
			ok = true;
			num2 =num* cont;
			aux = num2;
			while (aux != 0){
				pos = aux % 10;
				vector[pos] = true;
				aux /= 10;
			}
			for (int j = 0; j < TAM; ++j) ok = ok&&vector[j];
			++cont;
		}
		out << num2 << '\n';
	}

}