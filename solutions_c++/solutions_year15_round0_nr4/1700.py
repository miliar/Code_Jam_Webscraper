#include<iostream>
#include<fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int main()
{
	int test;
	int X,R,C;
	fin>>test;
	for(int i=1;i<=test;i++)
	{
		fin>>X>>R>>C;
		if(X==1)
			fout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
		else
		{
			if(((R*C)%X)!=0)
				fout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
			else
			{
				if(X==2)
					fout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
				else
				{
					if((R==1)||(C==1))
						fout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
					else
					{
						if((R*C)==X)
							fout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
						else
						{
							if((R<(X-1))||(C<(X-1)))
								fout<<"Case #"<<i<<": "<<"RICHARD"<<endl;
							else
								fout<<"Case #"<<i<<": "<<"GABRIEL"<<endl;
						}
					}
				}
			}
		}
	}
	return 0;
}
