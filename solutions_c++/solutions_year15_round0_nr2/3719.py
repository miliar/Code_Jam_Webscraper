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
int t,d;
vector <int> p;
int main()
{
	in >> t;
	for(int i=1;i<=t;i++)
	{
		in >> d;
		p.resize(d);
		int z = 0;
		for (int j=0;j<d;j++) {
			in >> p[j];
			z += p[j];
		}
		for (int j=1;j<=1000;j++) {
			int y = j;
			for (int k=0;k<d;k++) {
				y += (p[k]-1)/j;
			}
			z = min(z, y);
		}
		out << "Case #" << i << ": " << z << "\n";
	}
	return 0;
}
