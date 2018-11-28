#include <fstream>
#include <vector>
#include <string>

using namespace std;

const short int TAM = 10;

void resol(int i, ifstream & in, ofstream & out);
vector<bool> maneuver(vector<bool> const&v);

int main(){
	ifstream in; ofstream out;
	in.open("D-small-attempt0.in");
	out.open("D-small-attempt0.out");
	int nCase;
	in >> nCase;
	for (int i = 0; i < nCase; ++i)
		resol(i, in, out);
	in.close();
	out.close();
	return 0;
}

void resol(int i, ifstream & in, ofstream & out){
	out << "Case #" << i + 1 << ":";
	int k, c, s;
	in >> k >> c >> s;
	for (int i = 0; i < s; ++i) out << ' ' << i + 1;
	out << '\n';
}