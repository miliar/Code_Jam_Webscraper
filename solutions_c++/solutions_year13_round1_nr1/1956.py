#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

//#define PI 3.1415926535897932384626433832795

using namespace std;

int main()
{
	string name("A-small-attempt0");
	ifstream in;
	ofstream out;
	int nbCases = 0; // size of the sets loaded
	// Variables end -------------------------------------------------------------------------

	in.open((name + ".in").c_str());
	out.open((name + ".out").c_str()); // flux opening

	if(!(in.is_open() && out.is_open()))
	{
		cerr << "> one of the file could not be loaded" << endl;
	}

	in >> nbCases; // getting case number
cout.setf ( std::ios::fixed);

	for(int c=1;c<=nbCases;c++)
	{
		long long paint, remPaint, lastSurface, surface;
		long long nb, baseR, r;

		in >> baseR >> paint;
		remPaint = paint; r = baseR;
		nb=0;
		do
		{
			lastSurface = r*r;
			surface = (r+1)*(r+1);
			remPaint-= surface-lastSurface;
			//cout << "rempaint : " <<  remPaint << " surface : " << surface << endl;
			if(remPaint>=0)
				nb++;

			r+=2;
 //cin.get();
		}while(remPaint>=0);

		out << "Case #" << c << ": " << nb << endl;
		cout << "Case #" << c << ": " << nb << endl;
	}

    in.close();
    out.close();
    cout << "Appuyez sur ENTER pour continuer" << endl;
    cin.get();
    return 0;
}
