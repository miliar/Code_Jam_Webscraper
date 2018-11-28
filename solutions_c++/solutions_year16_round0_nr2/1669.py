

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>


using namespace std;

class Problem {
private:
public:
	Problem(string stos, int ktory, ofstream& g) {
		int index = stos.length();
		string pomoc = "";
		char c;
		int suma = 0;
		while (index >= 0) {
			if (stos[index] == '-') {
				suma++;

				pomoc = stos.substr(0, index+1);
				stos = "";
				for (int i = 0; i <pomoc.length(); i++) {
					if (pomoc[i] == '-')
						c = '+';
					else
						c = '-';
					stos += c;
				}
				index = stos.length();
			}
			index--;
		}
		g << "Case #" << ktory << ": " << suma << endl;
	}

};

int main()
{
	ifstream f;
	ofstream g;
	int problems = 0;
	Problem* p;
	string stos="";
	long int n = 0, k = 0;
	f.open("A-small-problem.in");
	g.open("Answer.out");

	f >> problems;
	for (int i = 0; i < problems; i++) {
		f >> stos;
		p = new Problem(stos, i + 1, g);
		stos = "";
		delete p;
	}
	f.close();
	g.close();
	return 0;
}

