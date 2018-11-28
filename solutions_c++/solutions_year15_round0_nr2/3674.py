#include <fstream>
#include <iostream>
using namespace std;

const int N = 1 + 1e4;

int v[N], n;

int compute(int eat){
	int ans = 0;
	for (int i = 1; i <= n; i++)
		ans += (v[i] - 1) / eat;
	return ans;
}

int solve(ifstream& in){
	int M = 0;

	in >> n;
	for (int i = 1; i <= n; i++){
		in >> v[i];
		M = max(M, v[i]);
	}

	int best = M;
	for (int eat = 1; eat <= M; eat++)
		best = min( best, compute(eat) + eat );
	return best;
}

int main(int argc, char** argv){
	ifstream in(argv[1]);
	ofstream out(argv[2]);
	int times;

	in >> times;
	for (int t = 1; t <= times; t++)
		out << "Case #" << t << ": " << solve(in) << '\n';
	return 0;
}
