#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int t,i,x,r,c,ans,s;
	ifstream fin("8.txt");
	ofstream fout("9.txt");
	fin >> t;
	for (i=0;i<t;i++)
	{
		fin >> x >> r >> c;
		s=r*c;
		if (r < x && c <x)
		{
			ans=0;
		}
		else
		{
			switch(x)
			{
				case 1: ans=1;break;
				case 2:
					if (s==3 || s==9)
					{
						ans=0;
					}
					else ans=1;
					break;
				case 3:
					if (s==3 || s==4 || s==8 || s==16)
					{
						ans=0;
					}
					else ans=1;
					break;
				case 4:
					if (s==4 || s==8)
					{
						ans=0;
					}
					else ans=1;
			}
		}
		if (ans==1)
		{
			fout << "Case #"<<i+1<<": GABRIEL" << endl;
		}
		else fout << "Case #"<<i+1<<": RICHARD" << endl;

	}
	return 0;
}