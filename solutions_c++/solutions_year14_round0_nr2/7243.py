#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <cstddef>
#include <vector>
#define LL long long
#define ULL unsigned long long


using namespace std;

int main (){
	ifstream in ("input.in");
	ofstream out ("output.out");
	out.precision (26);
	int t;
	in >> t;
	for (int i=0; i<t; i++)
	{
		double time = 0, c, f, x, speed = 2;
		in >> c >> f >> x;
		while (x*1./speed > x*1./(speed+f) + c*1./(speed)){
			time += c*1./(speed);
			speed += f;
		}
		out << "Case #" << i+1 << ": " << time + x*1./speed << '\n';
	}

	in.close();
	out.close();
	return 0;
}