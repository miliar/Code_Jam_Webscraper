#include <fstream>
#include <cmath>
#include <string>
#include <cstdlib>
#include <iostream>
using namespace std;

int atoi(const string & s)
{
    return atoi(s.c_str());
}

unsigned long long int limit=2;

int main() {

	for (int i=2;i<=40;i++) limit*=2;

	ifstream input("input.txt");
	ofstream out("out.txt");
	int t;
	input >> t;
	string line;
	for (int i=1;i<=t;i++) {
		input >> line;
		string a,b;
		a = line.substr(0,line.find("/"));
		b = line.substr(line.find("/")+1,line.length());
		unsigned long long p,q;
		p = atoi(a);
		q = atoi(b);
		//cout << limit << " " << p << " " << q;
		//double x = ((double)limit/q)*p;
		//cout << x << endl;
		if (fmod((double)(((double)limit/q)*p),1.0)!=0) out << "Case #" << (i) << ": impossible" << endl;
		else {
			if (p>=q) out << "Case #" << (i) << ": 0" << endl;
			else {
				double solution = ceil((double)(log((double)((double)q/p))/(log(2.0))));
				out << "Case #" << (i) << ": " << solution << endl;
			}
		}
	}
	system("PAUSE");
	out.close();
	return 0;
}