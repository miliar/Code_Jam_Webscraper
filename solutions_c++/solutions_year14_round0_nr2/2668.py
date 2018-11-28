#include<iostream>
#include<fstream>
#include<iomanip>
int main()
{
	std::ifstream in;
	in.open("B-large.in");
	std::ofstream out;
	out.open("B-large.out");
	int T, c=0;
	double C, F, X, D, t1, t2, t;
	in>>T;
	while(T--)
	{
		c++;
		t = 0;
		D = 2;
		in>>C>>F>>X;
		if(X <= C)
		{
				t1 = X/D;
		}
		else
		{
			t1 = X/2;
			
			t += C/D;
			t2 = t + X/(D+F);
			D += F;
			while(t1 > t2)
			{
				t1 = t2;
				
				t2 = t + C/D + X/(D+F);
				t += C/D;
				D += F;
			}
		}

		out<<"Case #"<<c<<": ";
		out << std::fixed;
		out << std::setprecision(7);
		out<<t1<<"\n";
	}
}