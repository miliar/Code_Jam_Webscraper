#include<iostream>
#include<fstream> 
using namespace std;

int main()
{
	ifstream f;
	ofstream f1;
	f.open("E:\\learn for fun\\code jam\\2015\\QB\\B-small-attempt4.in");
	f1.open("E:\\learn for fun\\code jam\\2015\\QB\\1.out");
	int t,i,j,k,max,result,temp,d;
	int p[60];
	f>>t;
	for (i=0;i<t;i++)
	{
		f>>d;
		for (j=0;j<d;j++) f>>p[j];
		for (j=d;j<60;j++) p[j]=0;
		for (j=0;j<d;j++)
		{
			for (k=j+1;k<d;k++)
			{
				if (p[j]<p[k])
				{
					temp=p[j];
					p[j]=p[k];
					p[k]=temp;
				}
			}
		}
		if (p[0]<=3) result = p[0];
		if (p[0]==4) 
		{
			if (p[1]>=3) result = 4;
			else result = 3;
		}
		if (p[0]==5)
		{
			if (p[1]>=4) result = 5;
			else result = 4;
		}
		if (p[0]==6)
		{
			if (p[1]<=3) result = 4;
			if (p[1]==4) result = 5;
			if (p[1]>=5)
			{
				if (p[2]<=3) result = 5;
				else result = 6;
			}
		}
		if (p[0]==7)
		{
			if (p[1]<=4) result = 5;
			if (p[1]==5) result = 6;
			if (p[1]==6)
			{
				if(p[2]>=5) result = 7;
				else result = 6;
			}
			if (p[1]==7)
			{
				if (p[2]>=5) result = 7;
				else result = 6;
			}
		}
		if (p[0]==8)
		{
			if (p[1]<=4) result = 5;
			if (p[1]==5) result = 6;
			if (p[1]==6)
			{
				if (p[2]<=4) result = 6;
				else result = 7;
			}
			if (p[1]==7)
			{
				if (p[2]<=4) result = 6;
				if (p[2]==5) result = 7;
				if (p[2]==6) 
				{
					if (p[3]<=4) result = 7;
					else result = 8;
				}
				if (p[2]==7)
				{
					if (p[3]<=4) result = 7;
					else result = 8;
				}
			}
			if (p[1]==8)
			{
				if (p[2]<=4) result = 6;
				if (p[2]==5) result = 7;
				if (p[2]==6)
				{
					if (p[3]<=4) result = 7;
					else result = 8;
				}
				if (p[2]==7)
				{
					if (p[3]<=4) result = 7;
					else result = 8;
				}
				if (p[2]==8)
				{
					if (p[3]<=4) result = 7;
					else result = 8;
				}
			}
		}
		if (p[0]==9)
		{
			if (p[1]<=3) result = 5;
			if (p[1]==4 || p[1]==5) result = 6;
			if (p[1]==6)
			{
				if (p[2]<=3) result = 6;
				else result = 7;
			}
			if (p[1]==7)
			{
				if (p[2]<=5) result = 7;
				else result = 8;
			}
			if (p[1]==8)
			{
				if (p[2]<=5) result = 7;
				if (p[2]==6)
				{
					if (p[3]==6) result = 9;
					else result = 8;
				}
				if (p[2]==7)
				{
					if (p[3]>=6) result = 9;
					else result = 8;
				}
				if (p[2]==8)
				{
					if (p[3]>=6) result = 9;
					else result = 8;
				}
			}
			if (p[1]==9)
			{
				if (p[2]<=5) result = 7;
				if (p[2]==6) result = 8;
				if (p[2]>=7)
				{
					if (p[3]<=5) result = 8;
					else result = 9;
				}
			}
		}
		f1<<"Case #"<<i+1<<": "<<result<<endl;
	}
	return 0;
}
