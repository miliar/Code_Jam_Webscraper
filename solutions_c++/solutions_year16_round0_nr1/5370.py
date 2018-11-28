#include <iostream>

using namespace std;

void main()
{
	int t, n, ti, i, ni, p, nip;
	int x[] = { 1,2,4,8,16,32,64,128,256,512 };
	cin >> t;
	for (ti = 1; ti <= t; ti++)
	{
		cin >> n;
		if (n != 0)
		{
			p = 0;
			for (i = 1; p != 1023; i++)
			{
				nip = ni = n * i;
				while (nip > 0)
				{
					p |= x[nip % 10];
					nip /= 10;
				}
			}
			cout << "Case #" << ti << ": " << ni << endl;
		}
		else
			cout << "Case #" << ti << ": INSOMNIA" << endl;
	}
}

