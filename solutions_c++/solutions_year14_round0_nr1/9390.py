#include <iostream>
#include <fstream>
#include <set>
#include <algorithm>
#define nmax 105
using namespace std;

int t, row, x;
set <int> S[2], intersect;

int main() {
	ifstream f("magic_trick.in");
	ofstream g("magic_trick.out");

	f>>t;
	for(int T=1; T<=t; T++) {
		S[0].clear();
		S[1].clear();
		intersect.clear();

		for(int arrangement=0; arrangement<=1; arrangement++) {
			f>>row;

			for(int i=1; i<=4; i++)
				for(int j=1; j<=4; j++) {
					f>>x;
					if(i == row) S[arrangement].insert(x);
				}
		}
		set_intersection(S[0].begin(), S[0].end(), S[1].begin(), S[1].end(), std::inserter(intersect,intersect.begin()));
		g<<"Case #"<<T<<": ";

		if(int(intersect.size()) == 1) g<<*intersect.begin()<<"\n";
		if(int(intersect.size()) == 0) g<<"Volunteer cheated!\n";
		if(int(intersect.size()) >= 2) g<<"Bad magician!\n";
	}

	return 0;
}

