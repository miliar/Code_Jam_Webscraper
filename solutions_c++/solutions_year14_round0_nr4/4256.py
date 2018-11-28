#include <iostream>
#include <vector>
#include <limits>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <iomanip> 
#include <fstream>

using namespace std;

void disp(string s, int r, int c, ofstream& ops)
{
	for(int i = 0; i < r; i++)
	{
		for(int h = 0; h < c; h++)
		{
			ops << s[i * c + h];
		}
		ops << endl;
	}
}

int main()
{
	ifstream ins("C:\\Users\\Mike\\Downloads\\A-small-attempt1 (1).in");
	ofstream ops("C:\\Users\\Mike\\Downloads\\output.txt");
	//istream& ins = cin;
	int t;
	ins >> t;

	for(int g = 0; g < t; g++)
	{
		ops << "Case #" << (g + 1) << ": ";
		int n;
		ins >> n;
		vector<double> ns(n);
		vector<double> ks(n);
		for(int i = 0; i < n; i++)
			ins >> ns[i];
		for(int i = 0; i < n; i++)
			ins >> ks[i];
		sort(ns.begin(), ns.end());
		sort(ks.begin(), ks.end());
		vector<bool> used(n, false);
		int war = 0;
		for(int i = 0; i < n; i++)
		{
			int k;
			for(k = 0; k < n; k++)
			{
				if(ks[k] > ns[i] && !used[k])
					break;
			}
			if(k == n)
				war++;
			else
				used[k] = true;
		}
		int dec = 0;
		int nfront = 0, kfront = 0;
		for(int i = 0; i < n; i++)
		{
			if(ns[i] > ks[kfront])
			{
				kfront++;
				dec++;
			}
		}
		ops << dec << " " << war << endl;
	}
	ops.close();
	//cin.get();cin.get();
	return 0;
}