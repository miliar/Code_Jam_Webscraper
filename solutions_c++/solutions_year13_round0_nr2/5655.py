#include <iostream>
#include <vector>

using namespace std;

typedef std::vector<std::vector<unsigned int> > lawn_t;

static void get_next_case(istream& input, lawn_t* lawn)
{
	std::string line;
	lawn->resize(0);
	unsigned int m,n;

	input >> n;
	input >> m;
	input.ignore(255, '\n');

	for (int i = 0; i < n; ++i) {
		unsigned int x;
		std::vector<unsigned int> row;
		for (int j = 0; j < m; ++j) {
			input >> x;
			row.push_back(x);
		}
		input.ignore(255, '\n');
		lawn->push_back(row);
	}
}

static bool check_square(const lawn_t& lawn, int i, int j)
{
	bool line_ok = true;
	unsigned int h = lawn[i][j];
	const unsigned int N = lawn.size();
	const unsigned int M = lawn[0].size();

	// Check row...
	for (int x = 0; x < M; ++x) {
		if (lawn[i][x] > h) {
			line_ok = false;
			break;
		}
	}

	if (line_ok) {
		return true;
	}

	line_ok = true;
	// Check column...
	for (int x = 0; x < N; ++x) {
		if (lawn[x][j] > h) {
			line_ok = false;
			break;
		}
	}
	return line_ok;
}

static bool check_lawn(const lawn_t& lawn)
{
	// Single row lawns can always be generated.
	if ((lawn.size() < 2) || (lawn[0].size() < 2)) {
		return true;
	}

	// Otherwise just scan the interior squares.
	for (int i = 0; i < lawn.size(); ++i) {
		for (int j = 0; j < lawn[0].size(); ++j) {
			if (!check_square(lawn, i, j)) {
				return false;
			}
		}
	}
	return true;
}

int main(int argc, char *argv[])
{
	lawn_t lawn;
	unsigned int test_cases;
	cin.sync_with_stdio(false);
	bool res;

	cin >> test_cases;
	cin.ignore(255, '\n');

	if (!test_cases) {
		return 0;
	}

	for (int i = 0; i < test_cases; ++i) {
		get_next_case(cin, &lawn);
		res = check_lawn(lawn);
		cout << "Case #" << i + 1 << ": " << std::string((res) ? "YES" : "NO")  << endl;
	}
}
