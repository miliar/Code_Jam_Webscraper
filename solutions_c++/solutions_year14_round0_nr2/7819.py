#include <iostream>
#include <conio.h>
#include <fstream>
using namespace std;

ifstream input("B-large.in");
ofstream output("B-large.out");

void main()
{
	int T;
	double C, F, X;
	output.precision(7);
	output.setf(ios::fixed|ios::showpoint);

	input>>T;
	for(int t=0; t<T; t++)
	{
		double cpers=2;
		double second=0;

		input>>C>>F>>X;
		if(X<=C)
			second=X/cpers;
		else
		{
			while(1)
			{
				if((X/cpers)>((C/cpers)+(X/(cpers+F))))
				{
					second+=(C/cpers);
					cpers+=F;
				}
				else
				{
					second+=(X/cpers);
					break;
				}
			}
		}

		output<<"Case #"<<t+1<<": "<<second<<endl;
	}

	_getch();
}