#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

#define getmax(a, b) ((a)>(b)) ? (a) : (b)
#define getmin(a, b) ((a)<(b)) ? (a) : (b)

using namespace std;

double c,f,x,cr;

double time ()
{
    if (c/cr+x/(cr+f)<x/cr)
    {
        cr+=f;
        return c/(cr-f)+time();
    }
    else
        return x/cr;
}

int main()
{
	ios_base::sync_with_stdio(false);

	ifstream in ("B.in");
	ofstream out ("B.out");
	int t;
	in >> t;
	for (int ti=1; ti<=t; ti++)
	{
        cr=2;
        in >> c >> f >> x;
        out << "Case #" << ti << ": " << fixed << setprecision(7) << time() << '\n';
	}
	in.close();
	out.close();

}
