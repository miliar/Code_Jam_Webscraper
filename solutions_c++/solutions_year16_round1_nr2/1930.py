#include <iostream>
#include <set>
#include <map>
#include <list>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <numeric>

using namespace std;


int main(int argc, char** argv)
{
	if (argc != 3)
		return -1;

	ifstream in(argv[1]);
	ofstream out(argv[2]);

	int t;

	in >> t;

	for (int caseN = 1; caseN <= t; ++caseN) {
		out << "Case #" << caseN << ":";

		int n;
		in >> n;

		map<int, int> counts;

		for (int j = 0; j < 2*n-1; ++j) {
			for (int k = 0; k < n; ++k) {
				int v;
				in >> v;
				++counts[v];
			}
		}

		list<int> res;
		for (map<int, int>::iterator it = counts.begin(); it != counts.end(); ++it) {
			
			if (it->second % 2 == 1) {
				res.push_back(it->first);
			}
		}

		res.sort();

		for (list<int>::iterator it = res.begin(); it != res.end(); ++it) {
			out << " " << *it;
		}
		out << endl;
	}

	in.close();
	out.close();

    return 0;
}



