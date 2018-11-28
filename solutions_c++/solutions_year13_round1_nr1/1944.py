#include <iostream>
#include <fstream>

using namespace std;




int main()
{
	ifstream in;
	ofstream out;
	in.open("Input.txt");
	out.open("Output.txt");
	int tests = 0;
	in >> tests;

	for(int k = 1; k <= tests; k++)
	{
		unsigned long long radius = 0;
		unsigned long long paint = 0;
		in >> radius >> paint;
		unsigned long long circles = 0;
		unsigned long long previousArea = radius * radius;
		radius++;
		while(radius * radius - previousArea <= paint)
		{
			paint -= radius * radius - previousArea;
			previousArea = (radius + 1) * (radius + 1);
			radius += 2;
			circles++;
		}
	
		//finish output here
		out << "Case #" << k << ": " << circles << endl;
	}
	in.close();
	out.close();

	return 0;
}