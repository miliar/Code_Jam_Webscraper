#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int count, i;
	long double Time = 0, Farm, Increase, Target, Rate = 2.0,Check_Now,Check_Next;

	ifstream fin("B-large.in");
	ofstream fout("output_B_Large.txt");

	fin >> count;
	for (i = 0; i < count; i++)
	{
		fin >> Farm;
		fin >> Increase;
		fin >> Target;

		Check_Now = Target / Rate;
		Check_Next = (Farm / Rate) + Target / (Rate + Increase);
		while (Check_Next < Check_Now)
		{
			Time += (Farm / Rate);
			Rate += Increase;
			Check_Now = Target / Rate;
			Check_Next = (Farm / Rate) + Target / (Rate + Increase);
		}
		Time += (Target / Rate);

		fout.precision(9);
		fout << "Case #" << i + 1 << ": " << Time<<endl;
		Time = 0;
		Rate = 2;
	}

	return 0;
}