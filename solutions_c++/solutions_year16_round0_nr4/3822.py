#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
	ifstream in("D-small-attempt1.in");
	ofstream out("OUT.out");
	int T;
	in >> T;
	int K, C, S;
	for (int i = 0; i < T; ++i)
	{
		in >> K >> C >> S;
		out << "Case #" << i + 1 << ": ";
		for (int j = 0; j < S; ++j)
			out << j + 1 << " ";
		out << endl;
	}
}