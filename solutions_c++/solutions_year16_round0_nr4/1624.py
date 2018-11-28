

#include "stdafx.h"
#include <iostream>
#include <fstream>


using namespace std;

class Problem {
private:
public:
	Problem(int k, int c, int s, ofstream& g, int ktory) {
		g << "Case #" << ktory << ":";
		for (int i = 0; i < s; i++)
			g << " " << i + 1;
		g << endl;
	}
};

int main()
{
	ifstream f;
	ofstream g;
	int problems = 0;
	Problem* p;
	string stos = "";
	long int n = 0, k = 0;
	f.open("A-small-problem.in");
	g.open("Answer.out");

	f >> problems;
	for (int i = 0; i < problems; i++) {
		f >> n;
		f >> k;
		f >> n;
		p = new Problem(n, k, n, g, i + 1);
		delete p;
	}
	f.close();
	g.close();
	return 0;
}

