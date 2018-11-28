#include <algorithm>
#include <fstream>
#include <string>

using namespace std;

struct State {
	int R, P, S;
};

string build_solution(const State& state) {
	if (state.R + state.P + state.S == 2) {
		return (state.P ? "P"s : ""s) + (state.R ? "R"s : ""s) + (state.S ? "S"s : ""s);
	}
	State left, right;
	left = right = State{ state.R / 2, state.P / 2, state.S / 2 };
	if (state.S % 2 == 0) {
		++left.P;
		++right.R;
	}
	if (state.R % 2 == 0) {
		++left.P;
		++right.S;
	}
	if (state.P % 2 == 0) {
		++left.R;
		++right.S;
	}
	return build_solution(left) + build_solution(right);
}

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int T;
	in >> T;
	for (int test = 1; test <= T; test++) {
		out << "Case #" << test << ": ";
		int N, R, P, S;
		in >> N >> R >> P >> S;
		if (max({ R,P,S }) - min({ R,P,S }) > 1) {
			out << "IMPOSSIBLE\n";
			continue;
		}
		out << build_solution({ R,P,S }) << endl;
	}
	return 0;
}