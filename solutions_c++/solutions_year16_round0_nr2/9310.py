#include<iostream>
#include<fstream>
#include<string>

using namespace std;

bool test(string a);
void flip(string &a, int n);

void main()
	{
	int rep = 0;
	int a;
	string b;
	ifstream ifile("B-large.in");
	ofstream ofile("B-large.out");
	ifile >> a;
	
	for (int i = 0; i < a; i++)
		{
		ifile >> b;
		/*cout << b << endl;*/
		while (!test(b))
			{
			for (int j = (b.size() - 1) ; j >= 0; --j)
				{
				if (b[j] == '-')
					{
					/*cin.get();*/
					flip(b, j);
					/*cout << b << endl;*/
					rep++;
					break;
					}
				}
			}
		ofile << "Case #" << i+1 << ": " << rep << endl;
		rep = 0;
		}

	}


bool test(string a)
	{
	bool flag = true;
	/*cout << a.size();*/
	//cin.get();
	for (int i = 0; i < a.size(); i++)
		{
		if (a[i] == '+');
		else 
			flag = false;
		}
	return flag;
	}

void flip(string &a, int n)
	{
	
	for (int i = 0; i <  n+1; i++)
		{
		if (a[i] == '+')
			a[i] = '-';
		else if (a[i] == '-')
			a[i] = '+';
		}
	}