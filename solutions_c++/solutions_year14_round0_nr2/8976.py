using namespace std;
#include <fstream>
#include <string>
#include <cmath>


int main()
{
	ifstream in;
	ofstream out;
	string temp;
	int T;
	in.open("c:\\Users\\Mohammed\\Desktop\\GoogleCode\\B-large.in");
	out.open("c:\\Users\\Mohammed\\Desktop\\GoogleCode\\output.txt", ios::out);
	double F;
	double C;
	double X;
	double c = 0;
	double total = 0;
	double rate = 2;
	int n;
	int per;
	getline(in, temp);
	T = stod(temp);
	for(int i = 0; i < T; i++)
	{
		c = 0;
		total = 0;
		rate = 2;
		in >> C;
		in >> F;
		getline(in, temp);
		X = stod(temp);
		while(c < X)
		{
			if(C >= X)
			{
				total = total + X/rate;
				c = X;
			}
			if(C < X)
			{
				if((X/rate)<=((C/rate)+(X/(rate+F))))
				{ total = total + (X/rate); c = X; }
				else
				{ total = total + C/rate; c = 0; rate= rate + F; }
			}
		}
		n = 0;
		per = int(total);
		temp = to_string(per);
		n = temp.size() + 7;
		out.precision(n);
		out << "Case #" << i+1 << ": " << total <<endl;
	}
}