#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	ifstream infile;
	infile.open("A-small-attempt2.IN");
	ofstream outfile;
	outfile.open("outfinal.OUT");
	string tcases;
	getline(infile, tcases);
	//cout << tcases;
	int e=stoi(tcases);
	//cout << e;
	int frnd = 0; // friends will be invited
	int aud = 0;  // audience exists 
	for (int t = 1; t <= e; t++)
	{
		string cas;
		getline(infile, cas);
		string shy;
		shy = cas.substr(0, 1);
		int shymax = stoi(shy);
		frnd=0;
		aud = 0;
		for (int i = 0; i <= shymax; i++)
		{
			string s;
			s = cas.substr(i + 2, 1);
			int si = stoi(s);
			//cout << si << endl;
			int added=0;
			if (i > aud && si != 0)
			{
				added = i - aud;
				frnd = frnd + added;
			}
			aud = aud + si+added;
		}
		//cout << "case #" << t << ": " << frnd << endl;
		outfile << "Case #" << t << ": " << frnd << endl;
	}
	
	
}