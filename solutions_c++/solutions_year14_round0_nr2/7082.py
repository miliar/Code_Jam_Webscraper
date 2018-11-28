#include <iostream>
#include <string.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	ifstream at;
	at.open ("at.txt");
	ofstream it;
	it.open ("it.txt");
	
	int t;
	at>>t;

	int a[4][4];
	int s[4][4];

	for (int l=0;l<t;l++)
	{
		double c,f,x;
		double g=2;
		at >> c>>f>>x;

		double t=0;

		while ( ((c/g) + (x/(g+f))) < (x/g))
		{
			t += c/g;
			g += f;
		}
		
		t += x/g;
		it << std::fixed;

		it << std::setprecision(7) << "Case #"<< l+1 <<": "<< t << endl;
	}
	return 0;
}
