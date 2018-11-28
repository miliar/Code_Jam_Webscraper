#include <string>
#include <fstream>

int main()
{
	std::ifstream in("input.txt");
	std::ofstream out("output.txt");

	int T;
	in >> T;

	for (int t = 1; t <= T; t++)
	{
		std::string s;
		in >> s;

		std::string r;
		for (char c : s)
		{
			r = r.size() > 0 && c >= r[0]
				? c + r
				: r + c;
		}

		out << "Case #" << t << ": " << r << std::endl;
	}
}