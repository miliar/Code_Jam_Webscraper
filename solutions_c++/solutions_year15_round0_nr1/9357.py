#include "stdafx.h"

#pragma
using namespace std;

#include <iostream>
#include <fstream>
#include<conio.h>
void main()
{
	int cases, c=1;

	ifstream in("A-large.in");
	ofstream out("A-large.out");
	in>>cases;
	while(c <= cases)
	{
		int smax, p, friends=0, standing=0;
		char *peopleStr;
		
		in>>smax;
		peopleStr = new char[smax + 2];
		in>>peopleStr;

		for(p=0; p<=smax; p++)
		{
			char peopleChar[2];
			int people;

			peopleChar[0] = peopleStr[p];
			peopleChar[1] = '\0';
			people = atoi(peopleChar);

			if(standing >= p)
				standing += people;
			else
			{
				int needStanding = p - standing;
				friends += needStanding;
				standing += needStanding + people;
			}
		}
		out<<"Case #"<<c<<": "<<friends<<"\n";
		c++;
	}
	in.close();
	out.close();
}
