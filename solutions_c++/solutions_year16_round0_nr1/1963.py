#include <fstream>
#include <unordered_set>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	unsigned t = 0;

	ifstream input("input.in");
	ofstream output("output.out");

	input >> t;

	long long n;
	unordered_set<char> digits;
	for (int i = 1; i <= t; ++i)
	{
		input >> n;

		if (n == 0) {
			output << "Case #" << i << ": " << "INSOMNIA" << endl;
			continue;
		}

		auto m = n;
		while (true) 
		{
			auto s = to_string(m);
			digits.insert(s.begin(), s.end());

			if (digits.size() == 10)
				break;

			m += n;
		}
	
		output << "Case #" << i << ": " << m << endl;

		digits.clear();
	}
	
	input.close();
	output.close();

	return 0;
}