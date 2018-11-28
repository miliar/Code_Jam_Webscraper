#include <fstream>
#include <string>
using namespace std;
ifstream in("in.in");
ofstream out("out.txt");
	

double solve() {
	double c, f, x; 
	in >> c >> f >> x;
	int count = 1;
	double time = 0;
	double produce = 2.0;
	double answer = x / produce;
	while (true) {
		double newans = 0;
		produce = 2.0;
		for (int i = 0; i < count; i++) {
			newans += c / produce;
			produce += f;
		}
		newans += x / produce;
		if (newans > answer) break;
		answer = min(answer, newans);
		count++;
	}
	return answer;
}

int main() {
	int t;
	in >> t;
	for (int i = 0; i < t; i++) {
		double a = solve();
		out.precision(16);
		out << "Case #" << i + 1 << ": " << a << endl; 
	}
	return 0;
}