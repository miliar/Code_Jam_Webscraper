#include <cmath>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int T;
int N;
vector<bool> visited;
int digits;

bool complete(string s) {
	for(int i = 0; i < s.length(); i++) {
		int x = s.at(i) - '0';
		if(!visited[x]) {
			visited[x] = true;
			digits++;
		}
	}

	return digits == 10;
}

int getUpper(int n) {
	if(n == 0)
		return 0;

	return (int)pow(10, 2+(int)log10(n-0.001));
}

int main() {
	ifstream in("in.txt");
	ofstream out("out.txt");

	in >> T;

	for(int t = 1; t <= T; t++) {
		out << "Case #" << t << ": ";
		in >> N;
		visited = vector<bool>(N, false);
		digits = 0;

		bool done = false;

		int upper = getUpper(N);

		for(int i = 1; i <= upper; i++) {
			int val = i * N;
			stringstream ss;
			ss << val;
			string s = ss.str();
			if(complete(s)) {
				done = true;
				out << val << endl;
				break;
			}
		}

		if(!done) {
			out << "INSOMNIA" << endl;
		}
	}

	return 0;
}
