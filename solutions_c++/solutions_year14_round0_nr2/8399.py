#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std ;

int main()
{
	ifstream in;
	in.open("Cookie.in");

	ofstream out;
	out.open("Cookie.out");

	int N;
	in >> N;
	for(int i = 1 ; i <= N ; i ++)
	{
		double C,F,X;
		in >> C >> F >> X;
		double total = 0.0, cur = 2.0;
		for(; X / cur > X / (cur + F) + C / cur ; cur += F)
		{
			total += C / cur;
		}
		out << "Case #" << i << ": " << setprecision(20) << total + X / cur << endl;
	}
	return 0 ;
}