#include <iostream>  
#include <fstream>
#include <string>
using namespace std;  

void setarray(int n[])
{
	for (int i = 0; i < 10; i++)
	{
		n[i] = 0;
	}
}
bool checkarray(int n[])
{
	int a = 0;
	for (int i = 0; i < 10; i++)
	{
		if (n[i] == 1)
		{
			a++;
		}
	}
	if (a == 10)
		return true;
	else
		return false;
}
void setarray(int n[], int a)
{
	for (int i = a; i > 0; i = i / 10)
	{
		n[i % 10] = 1;
	}
}

void main() 
{
	ofstream myfile;
	ifstream inputfile("A-large.in");
	int t, n, m;
	string s;

	inputfile >> t;
	int a[10];
	myfile.open("example.txt");
	for (int i = 1; i <= t; ++i) {
		inputfile >> n;
		setarray(a);
		int count = 1;
		while (true)
		{
			if (checkarray(a))
			{
				myfile << "Case #" << i << ": " << n*(count - 1) << endl;
				break;
			}
			setarray(a, n*count);
			count++;
			if (n == n*count)
			{
				myfile << "Case #" << i << ": INSOMNIA" << endl;
				break;
			}
		}
	}
	myfile.close();
	inputfile.close();
}