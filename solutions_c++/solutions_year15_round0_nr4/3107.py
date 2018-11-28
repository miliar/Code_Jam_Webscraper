#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	ifstream in("D-small-attempt2.in");
	ofstream out("output2.txt");

	int T, X, R, C;
	const char *richard = "RICHARD";
	const char *gabriel = "GABRIEL";

	in >> T;

	for (int i = 1; i <= T; ++i)
	{
		in >> X >> R >> C;

		if (R==1 && C == 1)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==1 && C == 2)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==1 && C == 3)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==1 && C == 4)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==2 && C == 1)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==2 && C == 2)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==2 && C == 3)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==2 && C == 4)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==3 && C == 1)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==3 && C == 2)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==3 && C == 3)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==3 && C == 4)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}
		}

		else if (R==4 && C == 1)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==4 && C == 2)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << richard << endl;
			}
		}

		else if (R==4 && C == 3)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}
		}

		else if (R==4 && C == 4)
		{
			if (X == 1)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 2)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}

			else if (X == 3)
			{
				out << "Case #" << i << ": " << richard << endl;
			}

			else if (X == 4)
			{
				out << "Case #" << i << ": " << gabriel << endl;
			}
		}
	}
}