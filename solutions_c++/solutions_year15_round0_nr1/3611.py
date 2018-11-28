//#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	for (int t=0; t <T; t++) {
		int maxShy;
		in >> maxShy;
		int people(0), peopleAdded(0);
		for (int shyLevel = 0; shyLevel <= maxShy; shyLevel++) {
			char c;
			in >> c;
			int p = int(c) - int('0');
			if (p != 0) {
				if (shyLevel <= people) { //good
					people += p;
				}
				else {
					int extra = shyLevel - people;
					peopleAdded += extra;
					people += (extra + p);
				}
			}
		}
		out << "Case #" << t+1 << ": " << peopleAdded << endl;
	} //case
} //main