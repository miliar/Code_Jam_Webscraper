#include <iostream>
#include <fstream>
#include <string>
#include <assert.h>

using namespace std;
int g(0);


void flip(string & x, int end);

int main()
{
	fstream myfile, output;
	string myfilename;
	cout << "enterfilename" << endl;
	cin >> myfilename;
	myfile.open(myfilename, ios::in);
	output.open("output.txt", ios::out);
	int t;
	string x;
	myfile >> t;
	bool plus;
	assert(t >= 1 && t <= 100);
	for (int i = 0; i < t; i++)
	{
		myfile >> x;
		plus = false;
		assert(x.size() <= 100 && x.size() >= 1);
		while (!plus)
		{
			for (int i = 0;i < x.size();i++)
			{
				if (x[i] == '-') break;
				if (i + 1 == x.size())
				{
					plus = true;
					break;
				}
			}
			if (plus) break;
			if (x.size() == 1)
			{
				if (x[0] == '-')
				{
					x[0] = +1;
					g++;
				}
				plus = true;
			}
			else
			{
				for (int i = 0; i < x.size() - 1; i++)
				{
					if (!(x[i] == x[i + 1]))
					{
						flip(x, i + 1);
						}
					if (i + 1 == x.size() - 1 && x[i] == '-') {
						flip(x, i + 2);
						break;

					}
				}
			}
			
		}
		output << "Case #" << i + 1 << ": " << g << endl;
		cout << "Case #" << i + 1 << ": " << g << endl;
		g = 0;

	}
	myfile.close();
	output.close();
}
void flip(string & x, int end)
{
	g++;
	char temp;
	int middle = end/2;
	for (int i = 0; i < middle;i++)
	{
		temp = x[i];
		x[i] = x[end-1];
		x[end-1] = temp;
	}
	for (int i = 0; i < end;i++)
	{
		if (x[i] == '-') {
			x[i] = '+';
			continue;
		}
		if (x[i] == '+') x[i] = '-';
	}
}