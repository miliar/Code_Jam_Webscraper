#include <fstream>
using namespace std;

const int N = 1 + 1e4;

char s[N];

int solve(ifstream& in){
	int n, sum = 0, ans = 0;

	in >> n >> s;
	for (int i = 0; i <= n; i++){
		if ( sum < i ){
			ans += i - sum;
			sum = i;
		}
		sum += s[i] - '0';
	}
	return ans;
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
