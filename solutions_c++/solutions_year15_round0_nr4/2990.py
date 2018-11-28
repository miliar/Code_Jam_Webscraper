#include<iostream>
#include<fstream>
using namespace std;
void no(ofstream &fout,int num)
{
	fout<<"Case #"<<num+1<<":"<<" RICHARD\n";
}
void yes(ofstream &fout,int num)
{
	fout<<"Case #"<<num+1<<":"<<" GABRIEL\n";
}
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("in.txt");
	fout.open("out.txt");
	int num;
	
	int X,R,C;
	int counter=0;
	if(fin.is_open())
	{
		fin>>num;
		while(counter<num)
		{
			fin>>X;
			fin>>R;
			fin>>C;
			if(X>=7)
			{
				no(fout,counter);
			}
			else if((R*C)%X == 0 )
			{
				if((X-1<=R && X-1<=C))
				{
					no(fout,counter);

				}
				else
				{
					yes(fout,counter);
				}
			}
			else
			{
				no(fout,counter);
			}
			counter++;
		}
	}
	system("pause");
	return 0;
}