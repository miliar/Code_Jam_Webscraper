#include <iostream>
#include <sstream>
#include <unordered_set>
#include <vector>

using namespace std;

int main() {
	int64_t Ncase;
	cin >> Ncase;
	ostringstream output;
	for (int64_t i1 = 1; i1 <= Ncase; ++i1){
		string instr;
		cin >> instr;
		int N = instr.length();

		string str(N,'='), orderstr(2*N,'=');
		int start = N-1;
		int end = N;
		orderstr[start] = instr[0];
		for (int i = 1; i < N; ++i) {
			if (instr[i] >= orderstr[start]){
				orderstr[--start] = instr[i];
			} else {
				orderstr[end++] = instr[i];
			}
		}
		for(int i = start; i < end; ++i) {
			str[i-start] = orderstr[i];
		}
		output << "Case #" << i1 << ": " << str << endl;
	}
	cout << output.str();
	return 0;
}
