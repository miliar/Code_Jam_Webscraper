#include <iostream>
#include <fstream>
#include <cstdlib>
#include <iomanip>
using namespace std;

void main()
{
	int number, i = 1;
	double x, f, c, t;
	ifstream openfile("C:\\Users\\Gong\\Desktop\\B-large.in", ios::in);
	ofstream writefile("C:\\Users\\Gong\\Desktop\\output.txt", ios::out);
	openfile >> number;
	while (i <= number)
	{
		double t1 = 0, t2 = 0, sum = 0;
		int n = 0;
		openfile >> c >> f >> x;
		t1 = x / 2;
		do
		{
			sum += c / (2 + n*f);
			t2 = sum + x / (2 + (n + 1)*f);
			if (t2 <= t1)
				t1 = t2;
			n++;
		} while (t1 >= t2);

		writefile.setf(ios::fixed, ios::floatfield); 
		writefile.precision(7);
		writefile << "Case #" << i << ": " << t1 << endl;
		i++;
	}
}