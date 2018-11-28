#include <cstdio>
#include <fstream>
using namespace std;

int main() {
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T; // number of test cases
	in >> T;
	//fscanf(in, "%d", &T);
	for (int case_no = 1; case_no <= T; case_no++) {
		int S_max;
		in >> S_max;
		// fscanf(in, "%d", &S_max);
		int n_less_shy = 0; // running count of people less shy than the current shyness
		int n_to_hire = 0; // Number of people to hire to clap
		for (int shy_level = 0; shy_level <= S_max; shy_level++) {
			char digit;
			in >> skipws >> digit;
			// fscanf(in, " %c", &digit);
			int n_of_shy_level = digit - '0';
			if (n_to_hire + n_less_shy < shy_level) {
				n_to_hire += shy_level - n_less_shy - n_to_hire;
			}
			n_less_shy += n_of_shy_level;
		}
		out << "Case #" << case_no << ": " << n_to_hire << '\n';
		// fprintf(out, "Case :%d %d\n", case_no, n_to_hire);
	}
	in.close();
	out.close();
	return 0;
}