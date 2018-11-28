#include<iostream>
#include<fstream>
#include<vector>
#define s 10

using namespace std;
int size_cal(int a);
bool test(int a[]);
void ini(int a[]);

void main()
	{
	int a, b;
	ifstream ifile("A-large.in");
	ofstream ofile("A-large.out");
	ifile >> a;
	int v[s];
	

	for (int i = 1; i <= a; i++)
		{
		ini(v);
		int alpha = 2;
		ifile >> b;
		int c = b;
		if (b == 0)
			{
			ofile << "Case #" << i << ": " << "INSOMNIA\n";
			continue;
			}
		else
			{
			while (!test(v))
				{
				/*int size = size_cal(b);*/
				int temp = b,t;
				while(temp!=0)/*for (int j = 0; j < size; j++)*/
					{
					t=temp % 10;
					v[t] = t;
					temp /= 10;
					}
				b += c;
			
				alpha++;
				}
			b-=c;
			}
		ofile << "Case #" << i << ": " << b << endl;

		}
	}

void ini(int a[])
	{
	for (int i = 0; i < s; i++)
		{
		a[i] = ' ';
	
		}
	}

bool test(int a[])
	{
	bool flag = true;
	for (int i = 0; i < s; i++)
		{
		if (a[i] == i);
		else	
			{
			flag = false;
			return flag;
			}
		}
	return flag;

	}

int size_cal(int a)
	{
	int sk = 0;
	while (a != 0)
		{
		a %= 10;
		sk++;
		}
	return sk;
	}

