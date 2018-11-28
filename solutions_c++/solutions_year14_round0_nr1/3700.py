#include<iostream>
#include <fstream>
#include<conio.h>
using namespace std;
int main()
{
	ifstream inp("input.in");
	ofstream out("output.txt");
	int cases;
	inp>>cases;
	int p[4][4];
	int n[4][4];
	int c1,c2;
	int count;
	int card;
	for(int z=1;z<=cases;z++)
	{
		inp>>c1;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				inp>>p[i][j];
			}
		}
		inp>>c2;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				inp>>n[i][j];
			}
		}
		count=0;
		c1--;
		c2--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<=3;j++)
			{
				if((p[c1][i]-n[c2][j])==0)
				{
					count++;
					card=p[c1][i];
				}
			}
		}
		out<<"case #"<<z<<": ";
		if(count==1)
		{
			out<<card<<"\n";
		}
		else if(count>1)
		{
			out<<"Bad magician!\n";
		}
		else
		{
			out<<"Volunteer cheated!\n";
		}
		
	}
	inp.close();
	out.close();
	getch();
	return 0;
	
}

