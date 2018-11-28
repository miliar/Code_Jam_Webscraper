#include <fstream>
#include <iostream>

using namespace std;

int main(){
	ifstream input("input");
	int nr_cases;
	input >> nr_cases;
	long long int s_rad, s_paint;
	long long int nr_circles;
	for(int i = 0; i < nr_cases; ++i)
	{
		input >> s_rad;
		input >> s_paint;
		nr_circles = -1;
		while(s_paint >= 0)
		{
			s_paint -= (2*s_rad+1);
			s_rad+=2;
			++nr_circles;
		}
		cout << "Case #" << i+1 << ": " << nr_circles << endl;
	}
	return 0;
}
