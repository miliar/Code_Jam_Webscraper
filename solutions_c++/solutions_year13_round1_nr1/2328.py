#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;

void main() {



	ifstream file;
	ofstream out;
	out.open("out.txt");
	file.open("input.txt");
	int T;
	long long r,t,num;
	long double c,x,maxR;
	long long rrr;
	long long paint, rad,count;
	file >> T;
	for (int i=0; i<T;i++)
	{
		file >> r >> t;
		rad = r+1;
		paint = 0;
		count = 0;
		while (paint < t)
		{
			paint += rad*rad - (rad-1)*(rad-1);
			rad+=2;
			count+=1;
		}
		if (paint > t)
			count--;


		out << "Case #" << i+1 << ": " << count << endl;

	}
	file.close();
	out.close();
	system("pause");

}
