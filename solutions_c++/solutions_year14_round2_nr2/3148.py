#include<iostream>
#include<conio.h>
#include<string.h>
#include<fstream>
#include<string>
#include<iomanip>
#include<math.h>
using namespace std;

int h;
void tobinary(int[], int);
int todecimal(int[]);
void main()
{
	ifstream input("fff.txt", ios::in);
	ofstream output("ft.out", ios::out);
	int loops;
	input >> loops;
	for (int i = 0; i<loops; ++i)
	{
		int count = 0;
		int a, b, q,h1,h2;
		int binary1[10], binary2[10], binary3[10];
		double number;
		input >> a;
		input >> b;
		input >> q;
		for (int y = 0; y<a; ++y)
		{
			for (int z = 0; z<b; ++z)
			{
				tobinary(binary1, y);
				h1 = h;
				tobinary(binary2, z);
				h2 = h;
				if (h2 <= h1)
				{
					h = h2;
				}
				else
					h = h1;
				for (int i = 0; i<10; ++i)
				{
					binary3[i] = 0;
				}
				for (int i = 9; i>=h; --i)
				{
					binary3[i] = (binary2[i] && binary1[i]);
				}
				number = todecimal(binary3);
				if (number<q) ++count;
				
			}
		}
		output<<"Case #"<<i+1<<": "<<count<<"\n";
	}
	input.close();
	output.close();
	cout << "Success";
}


void tobinary(int array[], int integer)
{
	int k = 10;
	h = 9;
	for (int i = 0; i<10; ++i)
	{
		array[i] = 0;
	}
	while (integer>0)
	{
		array[k - 1] = integer % 2;
		integer = integer / 2;
		--k;
		h = k;
	}
}
int todecimal(int array[])
{
	double sum = 0;
	for (int i = 0; i<10; ++i)
	{
		sum += array[9- i] * pow(2,i);
		
	}
	return sum;
}