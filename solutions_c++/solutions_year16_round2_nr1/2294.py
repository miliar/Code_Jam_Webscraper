#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void resol(int i, ifstream & in, ofstream & out);

int main(){
	ifstream in; ofstream out;
	in.open("A-large.in");
	out.open("A-large.out");
	int nCase; char aux;
	in >> nCase;
	in.get(aux);
	for (int i = 0; i < nCase; ++i)
		resol(i, in, out);
	in.close();
	out.close();
	return 0;
}

void resol(int i, ifstream & in, ofstream & out){
	string str;
	vector<int> digit;
	getline(in, str);
	while (str.size() > 0){
		//ZERO
		size_t z = str.find("Z");
		while (z != string::npos){
			str.erase(str.begin() + z);
			str.erase(str.begin() + str.find("E"));
			str.erase(str.begin() + str.find("R"));
			str.erase(str.begin() + str.find("O"));
			digit.push_back(0);
			z = str.find("Z");
		}
		//TWO
		size_t w = str.find("W");
		while (w != string::npos){
			str.erase(str.begin() + w);
			str.erase(str.begin() + str.find("T"));
			str.erase(str.begin() + str.find("O"));
			digit.push_back(2);
			w = str.find("W");
		}
		//SIX
		size_t x = str.find("X");
		while (x != string::npos){
			str.erase(str.begin() + x);
			str.erase(str.begin() + str.find("S"));
			str.erase(str.begin() + str.find("I"));
			digit.push_back(6);
			x = str.find("X");
		}
		//EIGHT
		size_t g = str.find("G");
		while (g != string::npos){
			str.erase(str.begin() + g);
			str.erase(str.begin() + str.find("E"));
			str.erase(str.begin() + str.find("I"));
			str.erase(str.begin() + str.find("H"));
			str.erase(str.begin() + str.find("T"));
			digit.push_back(8);
			g = str.find("G");
		}
		//THREE
		size_t h = str.find("H");
		while (h != string::npos){
			str.erase(str.begin() + h);
			str.erase(str.begin() + str.find("T"));
			str.erase(str.begin() + str.find("R"));
			str.erase(str.begin() + str.find("E"));
			str.erase(str.begin() + str.find("E"));
			digit.push_back(3);
			h = str.find("H");
		}
		//SEVEN
		size_t s = str.find("S");
		while (s != string::npos){
			str.erase(str.begin() + s);
			str.erase(str.begin() + str.find("E"));
			str.erase(str.begin() + str.find("V"));
			str.erase(str.begin() + str.find("E"));
			str.erase(str.begin() + str.find("N"));
			digit.push_back(7);
			s = str.find("S");
		}
		//FIVE
		size_t v = str.find("V");
		while (v != string::npos){
			str.erase(str.begin() + v);
			str.erase(str.begin() + str.find("F"));
			str.erase(str.begin() + str.find("I"));
			str.erase(str.begin() + str.find("E"));
			digit.push_back(5);
			v = str.find("V");
		}
		//FOUR
		size_t f = str.find("F");
		while (f != string::npos){
			str.erase(str.begin() + f);
			str.erase(str.begin() + str.find("O"));
			str.erase(str.begin() + str.find("U"));
			str.erase(str.begin() + str.find("R"));
			digit.push_back(4);
			f = str.find("F");
		}
		//ONE
		size_t o = str.find("O");
		while (o != string::npos){
			str.erase(str.begin() + o);
			str.erase(str.begin() + str.find("N"));
			str.erase(str.begin() + str.find("E"));
			digit.push_back(1);
			o = str.find("O");
		}
		//NINE
		while (str.size()>0){
			str.erase(str.begin() + str.find("N"));
			str.erase(str.begin() + str.find("I"));
			str.erase(str.begin() + str.find("N"));
			str.erase(str.begin() + str.find("E"));
			digit.push_back(9);
		}
	}
	sort(digit.begin(),digit.end());
	out << "Case #" << i + 1 << ": ";
	for (size_t k = 0; k < digit.size(); ++k){
		 out << digit[k];
	}
	out << '\n';
}