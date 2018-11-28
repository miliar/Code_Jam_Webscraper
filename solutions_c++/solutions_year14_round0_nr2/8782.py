#include <iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
	fstream file("B-large.in", ios::in);
	ofstream ofile("output.txt", ios::out);
	
	double C, F, X;
	
	
	int c;
	file>> c;
	for (int k = 0; k < c; k++)
	{
		double cookies = 2;
		double total = 0, wintime = 0, t1, t2 ;
		file >> C;
		file >> F;
		file >> X;
		
		t1 = X/cookies;
		
		total = C / cookies;
		cookies = cookies + F;
		wintime = X / cookies;
		t2 = total + wintime;
		while (t1>=t2)
		{
			t1 = t2;
			
			total = total + (C / cookies);
			cookies = cookies + F;
			wintime = X / cookies ;
			t2 = total + wintime;

		}
		ofile << "Case #" << k + 1 << ": " <<setprecision(7)<<fixed << showpoint<< t1 << endl;
	
	}
	file.close();
	ofile.close();
}