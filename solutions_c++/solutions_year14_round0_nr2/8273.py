#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	ifstream in ("B.in");
	ofstream out ("B.out");
	out.precision(7);
	int T;
	in >> T;
	for (int t = 1; t <= T; t++)
	{
		double C,F,X,ans,prev;
		double production = 2.0;
		in >> C >> F >> X;
		prev = X/production;
		ans = (C/production) + (X/(production+F));
		production += F;
		while (ans < prev)
		{
			prev = ans;
			ans -= X/production;
			ans += C/production + X/(production+F);
			production += F;
			//cout << prev << " " << ans << endl;
		}
		//cout << endl;
		out << "Case #" << t << ": " << prev << endl;
	}	
	return 0;
}
