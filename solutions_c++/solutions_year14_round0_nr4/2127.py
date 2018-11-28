#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main()
{
	fstream plik;
	fstream out;
	out.open("out.txt");
	plik.open("plik.txt");
	int n;
	plik >> n;
	for (int i = 0; i < n; i++)
	{
		int x;
		plik >> x;
		vector<double> Naomi(x);
		vector<double> Ken(x);
		for (int j = 0; j < x; j++)
		{
			plik >> Naomi[j];
		}
		sort(Naomi.begin(), Naomi.begin() + x);
		for (int j = 0; j < x; j++)
		{
			plik >> Ken[j];
		}
		sort(Ken.begin(), Ken.begin() + x);
		vector<double> w_Naomi=Naomi;
		vector<double> w_Ken = Ken;
		vector<double> d_Naomi=Naomi;
		vector<double> d_Ken=Ken;
		int w = 0;
		int d = 0;
		int y = x;
		for (int j = 0; j < y; j=0)
		{
			int z = 0;
			while (w_Naomi[j] >= w_Ken[z] && z < w_Naomi.size())
			{
				z++;
				if (z == w_Naomi.size())
					break;
			}
			if (z < w_Naomi.size())
			{
				w_Naomi.erase(w_Naomi.begin() + j);
				w_Ken.erase(w_Ken.begin() + z);
			}
			y--;
		}
		w = w_Naomi.size();
		
		y = x;
		for (int j = 0; j < y; j = 0)
		{
			int z = 0;
			while (d_Ken[j] > d_Naomi[z] && z < d_Ken.size())
			{
				z++;
				if (z == d_Ken.size())
					break;
			}
			if (z < d_Ken.size())
			{
				d_Ken.erase(d_Ken.begin() + j);
				d_Naomi.erase(d_Naomi.begin() + z);
			}				
			y--;
		}
		d = Naomi.size()-d_Naomi.size();
		out <<"Case #"<<i+1<<": " << d << " "<< w << endl;
	}
}