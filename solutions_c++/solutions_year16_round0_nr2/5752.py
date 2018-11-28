#include <fstream>
#include <vector>
#include <string>

using namespace std;

const short int TAM = 10;

void resol(int i, ifstream & in, ofstream & out);
vector<bool> maneuver(vector<bool> const&v);

int main(){
	ifstream in; ofstream out;
	in.open("B-large.in");
	out.open("B-large.out");
	int nCase;
	in >> nCase;
	for (int i = 0; i < nCase; ++i)
		resol(i, in, out);
	in.close();
	out.close();
	return 0;
}

void resol(int i, ifstream & in, ofstream & out){
	out << "Case #" << i + 1 << ": ";
	string str;
	in >> str;
	vector <bool> v(str.size());
	for (size_t i = 0; i < str.size(); ++i){
		if (str.at(i) == '+') v[i] = true;
		else v[i] = false;
	}
	bool reg = true;
	int cont = 0;
	while (v.size()>0){
		while (v.size() > 0 && v[v.size() - 1] == reg) v.pop_back();
		if (v.size() > 0){
			if (v[0] == v[v.size() - 1]){
				v = maneuver(v);
				++cont;
			}
			else{
				++cont;
				reg = !reg;
				while (v.size() > 0 && v[v.size() - 1] == reg) v.pop_back();
				v = maneuver(v);
				++cont;
			}
		}
	}
	out << cont << '\n';
}

vector<bool> maneuver(vector<bool> const&v){
	vector<bool> aux(v.size());
	for (size_t i = 0; i < v.size(); ++i) aux[i] = !v[v.size() - 1 - i];
	return aux;
}