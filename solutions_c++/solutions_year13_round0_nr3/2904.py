#include <fstream>
#include <cmath>

using namespace std;

inline bool isfair(int X)
{
	if (X / 10 == 0)
		return true;
	else if (X / 10 <= 9)
	{
		if (X / 10 == X % 10)
			return true;
		return false;
	}
	else
	{
		if (X / 100 == X % 10)
			return true;
		return false;
	}
}

int main(int argc, char const *argv[])
{
	char * infile = "C-small-attempt0.in";
	char * outfile = "C-small-attempt0.out";
	ifstream in(infile);
	ofstream out(outfile);

	int T, t, A, B, a, b, count;
	in>>T;
	for (t = 1; t <= T; t++)
	{
		count = 0;
		in>>A>>B;
		a = sqrt(A);
		b = sqrt(B);
		if ( a * a < A)
			a += 1;
		for (; a <= b; a++)
		{
			if (isfair(a) && isfair(a*a))
				count++;
		}
		out<<"Case #"<<t<<": "<<count<<endl;
	}
	return 0;
}