
//ques 4

#include<iostream>
#include "conio.h"
#include<fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
	int total,X,R,C;
	fin>>total;
	for(int i=0;i<total;i++)
	{
		fin>>X>>R>>C;
		if(X==1)
			fout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
		else
		{
			if(((R*C)%X)!=0)
				fout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
			else
			{
				if(X==2)
					fout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
				else
				{
					if((R==1)||(C==1))
						fout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
					else
					{
						if((R*C)==X)
							fout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
						else
						{
							if((R<(X-1))||(C<(X-1)))
								fout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
							else
								fout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
						}
					}
				}
			}
		}
	}
	_getch();
	return 0;
}

