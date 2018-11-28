#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <set>
#include <functional>

using namespace std;

int an;

int minAn(int P, int Q)
{
	// imposible
	if (Q % 2) return -1;
	if (an > 40) return -1;
		
	if (P < Q/2)
	{
		an++;
		return minAn(P * 2, Q);
	}
	else if (P == Q/2)
	{
		return an;
	}
	else
	{
		int newP = P - (Q/2);
		int current = an;
		int result = minAn(newP, Q);
		if (result == -1 || result > 40)
			return -1;
		else
			return current;
	}

}

int main()
{
	int T;

	ifstream in;
	in.open("in");
	ofstream out;
	out.open("out");

	in >> T;
	for (int r = 1; r <= T; r++)
	{
		int P, Q;
		char bar;
		in >> P >> bar >> Q;

		an = 1;

		int result = minAn(P, Q);
		out << "Case #" << r << ": ";
		if (result == -1) out << "impossible" << endl;
		else out << result << endl;
	}

	in.close();
	out.close();

	return 0;
}