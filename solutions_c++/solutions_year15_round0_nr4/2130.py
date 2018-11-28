#include <iostream>
#include <cstring>

using namespace std;

int x,r,c;

string DUMB()
{
	switch(x)
	{
		case 1:
		{
			return "GABRIEL";
		}break;
		case 2:
		{
			if((r == 1 && c == 1) ||
			   (r == 1 && c == 3) ||
			   (r == 3 && c == 1) ||
			   (r == 3 && c == 3))
				return "RICHARD";
			else
				return "GABRIEL";
		}break;
		case 3:
		{
			if((r == 1 && c == 1) ||
			   (r == 1 && c == 2) ||
			   (r == 2 && c == 1) ||
			   (r == 2 && c == 2) ||
			   (r == 1 && c == 3) ||
			   (r == 3 && c == 1) ||
			   (r == 1 && c == 4) ||
			   (r == 4 && c == 1) ||
			   (r == 2 && c == 4) ||
			   (r == 4 && c == 2) ||
			   (r == 4 && c == 4))
				return "RICHARD";
			else
				return "GABRIEL";
		}break;
		case 4:
		{
			if((r == 4 && c == 4) ||
			   (r == 4 && c == 3) ||
			   (r == 3 && c == 4))
				return "GABRIEL";
			else
				return "RICHARD";
				
		}break;
	}
	return "";
}

int main()
{
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{	
		cin >> x >> r >> c;
		cout << "Case #" << i << ": " << DUMB().c_str() << endl;	
	}
}