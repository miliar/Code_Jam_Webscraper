#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;
	for (int t = 0; t < T; t++) {
		int n;
		in >> n;
		vector<string> words(n);
		for (int i=0; i < n; i++)
			in >> words[i];

		vector<int> indexes(n, 0);
		int total(0);
		bool failed = false;
		bool finalChar = false;
		do {
			char c = words[0][indexes[0]];
			vector<int> counts(n,0);
			for (int i=0; i < n; i++) {
				char curr = words[i][indexes[i]];
				bool ok = false;
				while (curr == c && indexes[i] != words[i].length()) {
					ok = true;
					indexes[i]++;
					curr = words[i][indexes[i]];
					counts[i]++;
				}
				if (!ok) {failed = true; break;}
				if (indexes[0] == words[0].length()) { //final
					finalChar = true;
					if (indexes[i] != words[i].length()) {failed = true; break;}
				}
				else if (indexes[i] == words[i].length()) {failed = true; break;}
			}
			int sum(0);
			for (int i=0; i < n; i++)
				sum += counts[i];
			double avg = double(sum)/n;
			int avInt = avg;
			if (avg -avInt >= 0.5)
				avInt++;
			for (int i=0; i < n; i++)
				total += abs(counts[i]-avInt);



		} while(!failed && !finalChar);


		out << "Case #" << t+1 << ": "; 
		if (!failed) out << total << endl;
		else out << "Fegla Won\n";
		//if (a == -1) out << "NOT POSSIBLE\n";
		//else out << a << endl;
	}//test
}//main