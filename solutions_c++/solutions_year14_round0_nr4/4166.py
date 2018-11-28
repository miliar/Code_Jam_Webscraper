#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
using namespace std;

bool canStart(set<double>& n, set<double>& k) 
{
	set<double>::iterator nit = n.begin();
	set<double>::iterator kit = k.begin();
	for (; nit != n.end(); ++nit, ++kit) {
		if (*nit < *kit) return false;
	}
	return true;
}

int main(int argc, char* argv[])
{
	string fname;
	std::cin >> fname;
	string ifname = fname + ".in";
	string ofname = fname + ".out";
	ifstream in(ifname.c_str());
	ofstream out(ofname.c_str());

	int T;
	in >> T;
	for (int i = 0; i < T; ++i) {
		int N;
		in >> N;
		set<double> naomi;
		set<double> ken;
		set<double> n1;
		set<double> k1;

		for (int j = 0; j < N; ++j) {
			double temp;
			in >> temp;
			naomi.insert(temp);
			n1.insert(temp);
		}
		
		for (int j = 0; j < N; ++j) {
			double temp;
			in >> temp;
			ken.insert(temp);
			k1.insert(temp);
		}

		int wonCheat = 0;
		for (int j = 0; j < N; ++j) {
			if (canStart(naomi, ken)) {
				wonCheat = N - j;
				break;
			}
			else {
				naomi.erase(naomi.begin());
				auto it = ken.end();
				it--;
				ken.erase(it);
			}
		}
		
		for (auto nit = n1.begin(); nit != n1.end();) {
			bool found = false;
			for (auto kit = k1.begin(); kit != k1.end(); ++kit) {
				if (*kit > *nit) {
					k1.erase(kit);
					found = true;
					break;
				}
			}
			if (found) {
				nit = n1.erase(nit);
				if (nit == n1.end() && nit == n1.begin())
					break;
			}
			else {
				nit++;
			}
		}

		out << "Case #" << i + 1 << ": " << wonCheat << " " << n1.size() << endl;
	}

	return 0;
}