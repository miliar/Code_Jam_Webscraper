#include <fstream>
using namespace std;

int main() {
	ifstream cin ("input.txt");
	ofstream cout ("output.txt");
	cout.precision(7);
	int T;
	cin >> T;
	for(int X = 0; X < T; X++) {
		double c, f, x;
		cin >> c >> f >> x;
		double prevx = -1;
		double cps = 2.0, timec = 0.0, timex = x / cps;
		do {
			prevx = timex;
			timec += c / cps;
			cps += f;
			timex = timec + x / cps;
		} while (prevx >= timex);
		cout << "Case #" << (X + 1) << ": ";
		cout << fixed << prevx;
		cout << "\n";
	}
	system("PAUSE");
	return 0;
}