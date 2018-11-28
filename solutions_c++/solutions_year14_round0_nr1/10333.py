#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main()
{
	clrscr();
	int T,o[100],l=0;
	ifstream fin("input.in");
	ofstream fout("output.txt");
	fin>>T;
	while(l<T)
	{
		int r1,r2,m[4][4],n1[4],n2[4],c=0,e;
		fin>>r1;
		for(int i=0;i<4;++i)
		for(int j=0;j<4;++j)
		{
			fin>>m[i][j];
			if(i+1==r1)
				n1[j]=m[i][j];
		}
		fin>>r2;
		for(i=0;i<4;++i)
		for(j=0;j<4;++j)
		{
			fin>>m[i][j];
			if(i+1==r2)
				n2[j]=m[i][j];
		}
		for(i=0;i<4;++i)
		for(j=0;j<4;++j)
		{
			if(n1[i]==n2[j])
			{
				c++;
				e=n1[i];
			}
		}
		if(c>1)
			o[l]=20;
		else if(c==0)
			o[l]=21;
		else
			o[l]=e;
		++l;
	}
	for(int i=0;i<l;++i)
	{
			if(o[i]==20)
				fout<<"\nCase #"<<i+1<<": "<<"Bad magician!";
			else if(o[i]==21)
				fout<<"\nCase #"<<i+1<<": "<<"Volunteer cheated!";

			else
				fout<<"\nCase #"<<i+1<<": "<<o[i];
	}
	fin.close();
	fout.close();
}