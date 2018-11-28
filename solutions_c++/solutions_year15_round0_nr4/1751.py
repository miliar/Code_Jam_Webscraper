#include <iostream>

using namespace std;

int t, x, r, c;

int main()
{
    cin >> t;
    for (int ca = 1; ca <= t; ca++)
    {
	cin >> x >> r >> c;
	bool can = true;
	if ((r * c) % x != 0)
	    can = false;
	if (x == 4 && (r * c <= 8))
	    can = false;
	if (x >= 3 && (r == 1 || c == 1))
	    can = false;
	cout << "Case #" << ca << ": ";
	if (can)
	    cout << "GABRIEL" << endl;
	else
	    cout << "RICHARD" << endl;
    }
}

	    
