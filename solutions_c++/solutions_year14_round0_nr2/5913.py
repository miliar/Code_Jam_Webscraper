#include <fstream>
#include <iomanip>
using namespace std;

int main() {

	ifstream input("input.txt");
	ofstream out("out.txt");
	int t;
	input >> t;
	for (int i=0;i<t;i++) {
		double c,f,x;
		input >> c >> f >> x;
		int farm = 0;
		double time = x/2.0;
		double c_time = 0.0;
		while (true) {
			double t=0.0;
			c_time += c / (2.0+(farm*f));
			t = c_time + (x / (2.0+(farm+1)*f));
			if (t < time) time = t;
			else break;
			farm++;
		}
		out << "Case #" << (i+1) << ": ";
		out << std::fixed << std::setprecision(7) << time << endl;
	}
	out.close();
	return 0;
}