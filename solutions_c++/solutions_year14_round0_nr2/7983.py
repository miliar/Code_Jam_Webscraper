#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <string>

using namespace std;

string readline(ifstream*);
vector<string> split(string*, char);

int main() {
	ifstream in("B-large.in", ios_base::in);
	ofstream out("output.out", ios_base::out);

	cout << fixed << setprecision(7);
	out << fixed << setprecision(7);

	int t = atoi(readline(&in).c_str());
	for (int i = 1; i <= t; i++) {
		string line = readline(&in);
		vector<string> data = split(&line, ' ');
		double c = atof(data[0].c_str()), f = atof(data[1].c_str()), x = atof(data[2].c_str());
		double time = 0, max = x / 2.0;
		double min = max;
		int n = 0;
		while (time < max) {
			time += c / (2 + f * n);
			n++;
			double remain = x / (2 + f * n);
			if (time + remain < min)
				min = time + remain;
			if (remain < 10e-7)
				break;
		}
		cout << "Case #" << i << ": " << min << "\n";
		out << "Case #" << i << ": " << min << "\n";
	}

	in.close();
	out.close();

	cin.ignore();
	return 0;
}

vector<string> split(string* s, char delim) {
	vector<string> result;
	stringstream ss(*s);
	string token;
	while (getline(ss, token, delim)) {
		result.push_back(token);
	}
	return result;
}

string readline(ifstream* in) {
	string result;
	getline(*in, result);
	return result;
}