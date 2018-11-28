#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdlib>
using namespace std;

void main()
{
	int number, i = 1;
	
	ifstream openfile("C:\\Users\\Gong\\Desktop\\B-small-attempt0.in", ios::in);
	ofstream writefile("C:\\Users\\Gong\\Desktop\\output.txt", ios::out);
	openfile >> number;
	while (i <= number)
	{
		int a, b, k;
		int count = 0;
		int t;
		openfile >> a >> b >> k;
		for (int o = 0; o < a;o++)
		for (int p = 0; p < b; p++)
		{
			t = o&p;
			if (t < k) count++;
		}
		writefile << "Case #" << i << ": " << count << endl;
		i++;
	}
	system("pause");
/*	int a = 10, b = 12;
	int c = a&b;
	cout << c;*/
	system("pause");
}