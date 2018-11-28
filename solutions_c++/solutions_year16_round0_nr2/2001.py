#include <fstream>
#include <string>

using namespace std;

void magic(string& s, int p) 
{
	auto ss = s.substr(0, p + 1);

	for (int i = 0; i < ss.length(); i++)
		if (ss[i] == '+')
			ss[i] = '-';
		else
			ss[i] = '+';

	reverse(ss.begin(), ss.end());

	s.replace(0, p + 1, ss);
}

int main(int argc, char** argv)
{
	unsigned t = 0;

	ifstream input("input.in");
	ofstream output("output.out");

	input >> t;
	string s;
	getline(input, s);

	string line;
	for (int i = 1; i <= t; ++i)
	{
		getline(input, line);

		auto counter = 0;
		int p = line.length() - 1;
		
		while (p >= 0) {
			if (line[p] == '-') {
				int j = -1;
				if (line[0] != '-') {
					for (j = 0; j <= p; j++)
						if (line[j] == '-') {
							j--;
							break;
						}

					magic(line, j);
					counter++;	
				}

				if (j != p) {
					magic(line, p);
					counter++;
				}
			}
				
			p--;
		}

		line.clear();

		output << "Case #" << i << ": " << counter << endl;
	}
	
	input.close();
	output.close();

	return 0;
}