#include <iostream>
#include <conio.h>
#include <fstream>
using namespace std;

ifstream input("A-large.in");
ofstream output("A-large.out");

void main()
{
	int t;
	input>>t;
	cout<<t;
	for(int i=1; i<=t; i++)
	{
		int smax;
		input>>smax;
		int *arr = new int[smax+1];
		input.get();
		for(int j=0; j<smax+1; j++)
		{
			char ch;
			input.get(ch);
			arr[j] = atoi(&ch);
		}
		int need = 0, have = arr[0];
		for(int j=1; j<smax+1; j++)
		{
			if(arr[j]!=0)
			{
				int tmpneed = j;
				if(tmpneed>have+need)
				{
					need += tmpneed - (have+need);
				}
				have += arr[j];
			}
		}
		output<<"Case #"<<i<<": "<<need<<endl;
	}
	cout<<"OK";
	_getch();
}