#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int k=1; k<=T; k++)
	{
		double C, F, X;
		cin >> C >> F >> X;
		double now = X/2.0;
		double next = C/2.0 + X/(2.0+F);
		int n = 1;
		while (next < now)
		{
			now = next;
			next = next + (C-X)/(2+n*F) + X/(2+(n+1)*F);
			n++;
		}
		cout<<setiosflags(ios::fixed);
		cout << "Case #" << k << ": " << setprecision(7) << now << endl;
	}
	return 0;
}
