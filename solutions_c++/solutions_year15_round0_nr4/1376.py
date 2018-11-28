#include <iostream>
using namespace std;

int main()
{
	int t,x,r,c,a;
	cin >> t;
	for(int i = 1 ; i <= t ; i++)
	{
		cin >> x >> r >> c;
		if(x == 1)
			cout << "Case #" << i << ": GABRIEL" << endl;
		else
		{
			a = r*c;
			if((a >= (x*(x-1))) && (a%x == 0))
				cout << "Case #" << i << ": GABRIEL" << endl;
			else
				cout << "Case #" << i << ": RICHARD" << endl;
		}

	}
}