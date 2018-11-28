#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

void generatePal(vector<int> &parpal, double bInf, double bSup)
{
	int pal;
	for(int i=1;i<=9;i++)
	{
		pal=i;
		if(pal>=bInf && pal <= bSup)
			parpal.push_back(pal);
	}
	for(int i=1;i<=9;i++)
	{
		pal=i+i*10;
		if(pal>=bInf && pal <= bSup)
			parpal.push_back(pal);
	}
	for(int i=1;i<=9;i++)
	{
		for(int j=1;j<=9;j++)
		{
			pal=i+j*10+i*100;
			if(pal>=bInf && pal <= bSup)
				parpal.push_back(pal);
		}
	}
}

bool isPal(int pal)
{
    int invPal=0, tmp=pal;

    while(tmp!=0)
    {
    	invPal*=10;
    	invPal+=tmp%10;
    	tmp/=10;
    }

	while(pal!=0)
	{
		if(pal%10!=invPal%10)
			return false;
		pal/=10; invPal/=10;
	}
	return true;
}

int main()
{
	string name("C-small-attempt0");
	ifstream in;
	ofstream out;
	int nbCases = 0; // size of the sets loaded

	vector<int> pal;
	int cpt, binf, bsup;
	// Variables end -------------------------------------------------------------------------

	in.open((name + ".in").c_str());
	out.open((name + ".out").c_str()); // flux opening

	if(!(in.is_open() && out.is_open()))
	{
		cerr << "> one of the file could not be loaded" << endl;
	}

	in >> nbCases; // getting case number

	for(int c=1;c<=nbCases;c++)
	{
		cpt=0;
		in >> binf >> bsup;

		pal.resize(0);
		generatePal(pal, sqrt(binf), sqrt(bsup));

		for(unsigned int i=0;i<pal.size();i++)
			if(isPal(pal[i]*pal[i]))
			{
				cpt++;
				cout << pal[i] << " ² = " << pal[i]*pal[i] << endl;
			}

		out << "Case #" << c << ": " << cpt << endl; // starts at 1
	}

    in.close();
    out.close();
    cout << "Appuyez sur ENTER pour continuer" << endl;
    cin.get();
    return 0;
}
