#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <math.h>
#include <set>
using namespace std;
ifstream in("in.txt");
ofstream out("out.txt");
int t,s;
string a;
int main()
{
	in >> t;
	for(int i=1;i<=t;i++)
	{
		in >> s;
		in >> a;
		int g = 0;
		int h = 0;
		for (int j=0;j<=s;j++) {
			h = max(h, j-g);
			g += (a[j]-'0');
		}
		out << "Case #" << i << ": " << h << "\n";
	}
	return 0;
}
