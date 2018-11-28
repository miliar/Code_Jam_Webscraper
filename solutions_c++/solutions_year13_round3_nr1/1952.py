#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
	string name("A-small-attempt1");
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

	for(int c=1;c<=nbCases;c++)
	{
		string word;
		int winSize, cpt=0, lastIndex=0;

		in >> word >> winSize;

		for(unsigned int i=0;i<=word.size()-winSize;i++)
		{
			//cout << "considering : " << word.substr(i, winSize) << endl;
			if(word.substr(i, winSize).find_first_of("aiueo") == string::npos)
			{
				int ibis = i-lastIndex;
				int tmp = word.size()-winSize-i;
				//cout << "values : " << tmp << " and " << lastIndex  << " i " << i<< endl;
				cpt+= 1 + ibis + tmp + ibis*tmp;
				lastIndex = i+1;
				//cout << "cpt :" << cpt << endl;
			}
		}

		out << "Case #" << c << ": " << cpt << endl; // starts at 1
	}

    in.close();
    out.close();
    //cout << "Appuyez sur ENTER pour continuer" << endl;
    //cin.get();
    return 0;
}
