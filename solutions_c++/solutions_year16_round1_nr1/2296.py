#include <fstream>
#include <string>

using namespace std;

string s;

string run(string s) {
	string ret = "";
	ret += s[0];
	for (int i = 1; i < s.length(); i++) {
		if (s[i] >= ret[0])
			ret = s[i] + ret;
		else
			ret = ret + s[i];
	}
	return ret;
}

int main() {
	int T;
	ifstream in("A-large.in");
	ofstream out("output.txt");
	in >> T;
	getline(in, s);
	for (int t = 0; t < T; t++) {
		getline(in, s);
		string ans = run(s);
		//output
		out << "Case #" << t + 1 << ": " << ans << endl;
	}
	in.close();
	out.close();
	return 0;
}