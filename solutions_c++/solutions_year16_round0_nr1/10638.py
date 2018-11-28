// ConsoleApplication1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <ctime>
#include <fstream>
#include <vector>
using namespace std;


int main()
{
	int t,a,B[10],sum=0;
	bool ug;
	ifstream fiin("input.txt", ios_base::in);
	fiin >> t;
	ofstream fout("output.txt", ios_base::out);
	for (int i = 0; i < t; i++)
	{
		fiin >> a;
		if (a == 0)
			fout << "Case #" << i+1 << ": " << "INSOMNIA"<<endl;
		else
		{
			int a1 = a;
			for (int i = 0; i < 10; i++)
			{
				B[i]=0;
			}
			ug = true;
			while (ug)
			{
				int a2 = a;
				while (a != 0)
				{
					B[a % 10] = 1;
					a = a /10;
				}
				a = a2;
				sum = 0;
				for (int i = 0; i < 10; i++)
				{
					sum = sum + B[i];
				}
				if (sum == 10)
				{
					fout << "Case #" << i+1 << ": " << a<<endl;
					ug = false;
				}
				a = a + a1;
			}
		}
	}
	fiin.close();
	fout.close();
	return 0;
}

