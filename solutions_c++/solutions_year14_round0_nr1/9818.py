// magic.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <fstream>
#include <sstream>
#include <iostream>
using namespace std;

const int oneBits[] = {
	0, //0000,0000
	1, //0000,0001
	1, //0000,0010
	2, //0000,0011
	1, //0000,0100
	2, //0000,0101
	2, //0000,0110
	3, //0000,0111
	1, //0000,1000
	2, //0000,1001
	2, //0000,1010
	3, //0000,1011
	2, //0000,1100
	3, //0000,1101
	3, //0000,1110
	4  //0000,1111
};

inline int CountOnes(unsigned char x)
{
    return oneBits[x&0x0f] + oneBits[x>>4];
}

int locateOne(int a)
{
	int pos = 0;
	while (a >>= 1) pos ++;
	return pos;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int round;
	int r1, r2;
	int a;
	int b;
	int c;
	int m1[16], m2[16];
	unsigned char *p;

	ifstream from("A-small-attempt0.in");

	if (!from)
	{
		cout << "Cannot open input file" << endl;
		return -1;
	}

	ofstream to("output.txt");

	if (!to)
	{
		cout << "Cannot open output file" << endl;
		from.close();
		return -1;
	}

	from >> round;

	for (int i = 0; i < round; i ++)
	{
		from >> r1;
		for (int j = 0; j < 4; j ++)
			from >> m1[j << 2] >> m1[(j << 2) + 1] >> m1[(j << 2) + 2] >> m1[(j << 2) + 3];

		from >> r2;
		for (int j = 0; j < 4; j ++)
			from >> m2[j << 2] >> m2[(j << 2) + 1] >> m2[(j << 2) + 2] >> m2[(j << 2) + 3];

		r1 = (r1 - 1) << 2;
		r2 = (r2 - 1) << 2;

		a = (1 << (m1[r1] - 1)) + (1 << (m1[r1 + 1] - 1)) + (1 << (m1[r1 + 2] - 1)) + (1 << (m1[r1 + 3] - 1));
		b = (1 << (m2[r2] - 1)) + (1 << (m2[r2 + 1] - 1)) + (1 << (m2[r2 + 2] - 1)) + (1 << (m2[r2 + 3] - 1));

		c = a & b;

		p = reinterpret_cast<unsigned char*>(&c);

		switch(CountOnes(p[0]) + CountOnes(p[1]))
		{
		case 0:
			to << "Case #" << i + 1 << ": Volunteer cheated!"<< endl;
			break;
		case 1:
			to << "Case #" << i + 1 << ": " << locateOne(c) + 1 << endl;
			break;
		default:
			to << "Case #" << i + 1 << ": Bad magician!" << endl;
		}
	}

	return 0;
}

