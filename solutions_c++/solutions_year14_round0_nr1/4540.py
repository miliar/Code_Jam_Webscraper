#include<iostream>
#include<conio.h>
#include<string.h>
#include<fstream>
#include<string>
#include<vector>
#include<utility>
using namespace std;
void main()
{
	ifstream priyam;
	ofstream fout;
	priyam.open("A-small-attempt7.in");
	fout.open("A-small-attempt7.out");
	int T=0,p[4][4],sol,c[2][4],k,ct=0,n;
		priyam>>T;
	for(int i=0;i<T;i++)
	{
		for(n=0;n<=1;n++)
		{
		priyam>>sol;
		for(int j=0;j<=3;j++)
		{
			for(int h=0;h<=3;h++)
			{
		priyam>>p[j][h];
			}
		}
		for(int g =0;g<=3;g++)
		{
        c[n][g]=p[sol-1][g];
		}
		}
		if(n==1)
			n=0;
		for(int o=0;o<=3;o++)
		{
		if(c[0][0]==c[1][o])
		{
			ct++;
		k=c[1][o];
		}if(c[0][1]==c[1][o])
		{
			ct++;
		k=c[1][o];
		}if(c[0][2]==c[1][o])
		{
			ct++;
		k=c[1][o];
		}if(c[0][3]==c[1][o])
		{
			ct++;
		k=c[1][o];
		}
		}
		if(ct==1)
			fout<<"Case #"<<i+1<<": "<<k<<"\n";
		if(ct==0)
			fout<<"Case #"<<i+1<<": Volunteer cheated! \n";
		if(ct>1)
			fout<<"Case #"<<i+1<<": Bad magician! \n";
	ct=0;
	}
	priyam.close();
	getch();
	}