#include <iostream>
using namespace std;

string studyCase();

int main(int argc, char* argv[])
{
	unsigned int numberOfCases = 0;
	string res;
	cin >> numberOfCases;
	for (int i = 0; i < numberOfCases; ++i)
	{
		res = studyCase();
		cout << "Case #" << i+1 << ": " << res << endl; 
	}
	return 0;
}

string studyCase()
{
	string res = "GABRIEL";
	unsigned int X, C, R;
	cin >> X;
	cin >> R;
	cin >> C;
	switch (X)
	{
		case 2:
			if (!(R % 2 == 0 || C % 2 == 0))
				return "RICHARD"; 
			break;
		case 3:
			if (! ((R == 2 && C == 3) || (C == 2 && R == 3) || (R == 3 && C == 3) || (R == 4 && C == 3) || (C == 4 && R == 3)) )
				return "RICHARD"; 
			break;
		case 4:
			if (R + C <= 6) 
				return "RICHARD"; 
			break;
		default:
			break;
	}
	return res;
}
