#include<iostream>
#include<fstream>
using namespace std;

int f(int a, int b)
{
	return b + ((a - 1) / b);
}
int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");
	int t;

	in >> t;

	for (int testcase = 1; testcase <= t; ++testcase)
	{
		int r, c, w, x;
		int ans = 0;
		in >> r >> c >> w;
		
		if (c == w) ans = w;
		else{
			ans = f(c, w);
		}
		out << "Case #" << testcase << ": " << ans << endl;
	}


	in.close();
	out.close();

	return 0;
}
