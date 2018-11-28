#include <iostream>
using namespace std;



int main ()
{
	int cases;

	int t, r;

	cin >> cases;

	for (int i = 0; i < cases; ++i)
	{
		cin >> r >> t;

		int nrings = 0;

		while (1)
		{
			t -= ((r+1)*(r+1) - r*r);
			if (t < 0)
			{
				break;
			}
			else
			{
				nrings++;
			}
			r+=2;
		}

		cout << "Case #" << i+1 << ": " << nrings << endl;
	}
}