#include <iostream>
#include <string>
#include <fstream>
using namespace std;
bool CheckOmino(int X, int R, int C)
{
	bool var;
	//false means Richard Wins
	//true means Gabrial Wins
	if (X == 4)
	{
		if ((R == 4 && C == 4) || (R == 4 && C== 3) || (R == 3 && C == 4))
			return true;
		else
			return false;
	}
	else if (X == 3)
	{
		if (R<X && C<X)
			return false;
		else if ((R == 4 && C == 4) || (R == 2 && C == 4) || (R == 3 && C == 1) || (R == 4 && C == 1) || (R == 4 && C == 2) || (R == 1 && C == 3) || (R == 1 && C == 4))
			return false;
		else
			return true;
	}
	else if (X == 2)
	{
		if ((R == 3 && C == 1) || (R == 1 && C == 3) || (R == 3 && C == 3) || (R<X && C<X))
			return false;
		else
			return true;
	}
	else if (X == 1)
	{
		return true;
	}
}
int main()
{
	ifstream in("D-small-attempt2.in");
	ofstream out("result.out");
	int count;
	in >> count;
	for (int i = 0; i<count; i++)
	{
		int X, R, C;
		in >> X >> R >> C;
		bool var = CheckOmino(X, R, C);
		if (var == false)
			out << "Case #" << i + 1 << ": " << "RICHARD" << endl;
		else
			out << "Case #" << i + 1 << ": " << "GABRIEL" << endl;

	}
	in.close();
	out.close();
	return 0;
}