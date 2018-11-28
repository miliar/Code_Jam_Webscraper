#include <iostream>
#include <string>
#include <fstream>
#include <sstream>

using namespace std;

bool checksqr(int x, int y){

	if (x == y)
	{
		return false;
	}
	else if (x < y){
		if (y % x == 0)
		{
			return false;
		}
	}

	return true;
}

bool checkxrc(int x, int r, int c){
	if (x == 1)
	{
		return false;
	}
	else if (x == 2)
	{
		if (r == 1){
			return checksqr(x, c);
		}
		else if (c == 1)
		{
			return checksqr(x, r);
		}
	}

	int dim = r * c;
	if (x > dim || dim % x != 0)
	{
		return true;
	}
	else
	{
		if (x >= 3)
		{

			int max = x - 2;
			
			if (!((r > max && c >= 3 ) || (c > max && r >= 3)))
			{
				return true;
			}

		}

		return false;
	}
}


int main(){

	ifstream ifz("a.txt");
	ofstream ofz("b.txt");

	if (ifz.is_open() && ofz.is_open())
	{

		int icase;
		string s;

		getline(ifz, s);
		stringstream(s) >> icase;

		for (int i = 1; i <= icase; i++)
		{

			int x, r, c;
			stringstream ss;

			getline(ifz, s);
			ss.str(s);

			ss >> x;
			ss >> r;
			ss >> c;

			bool ans = checkxrc(x, r, c);

			ofz << "Case #" << i << ": ";

			if (ans)
			{
				ofz << "RICHARD";
			}
			else
			{
				ofz << "GABRIEL";
			}
			ofz << endl;
		}

	}
	int z;
	cin >> z;
}
