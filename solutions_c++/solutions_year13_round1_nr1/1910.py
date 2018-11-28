//============================================================================
// Name        : CodeJam.cpp
// Author      : Shadowvein
// Description : Google Code Jam Round 1A
//============================================================================

#include "Helper.h"

int RING_WIDTH = 1;

unsigned long calculateArea(unsigned long r)
{
	return 2 * r + 1;
}

void round1()
{
	int size = inputs.size();

	if (size == 0) exit(0);

	int testCaseNum = inputs[0];
	int i = 1;
	unsigned long radius;
	unsigned long paint;
	unsigned long area;
	unsigned long numCircles;

	do
	{
		radius = inputs[i];
		paint = inputs[i+1];
		i = i + 2;

		numCircles = 0;
		do
		{
			area = calculateArea(radius);

			if (paint >= area)
			{
				paint = paint - area;
				radius = radius + 2;
				numCircles++;
			}
		}
		while (paint >= area);

		outputs.push_back(numCircles);
	}
	while(i < size);

//	for (vector<string>::iterator it = inputs.begin() ; it != inputs.end(); it++)
//		outputs.push_back(*it);
}

// argv[1] = input file; argv[2] = output file
int main(int argc, char **argv)
{
	ofstream outputfile;
	outputfile.open(argv[2]);

	readFile(argv[1]);
	round1();
	writeFile(argv[2]);

//	int a[] = {12,10,43,23,-78,45,123,56,98,41,90,24};
//	int num;
//
//	num = sizeof(a)/sizeof(int);
//
//	int b[num];
//
//	mergesort(a,b,0,num-1);
//
//	for(int i=0; i<num; i++)
//		cout<<a[i]<<" ";
//	cout<<endl;

	return 0;
}
