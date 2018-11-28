#include <bits/stdc++.h>
using namespace std;
int main()
{
	double c,f,x,temp,t;
	int cnt=1,j,flag;
	string s;
	fstream fin;
	fin.open("B-large.in",ios::in);
	fstream fout;
	fout.open("output_codejam2.out",ios::out);
	if(fin.is_open())
	{
		j=0;flag=1;
		while(getline(fin,s))
		{
			istringstream iss(s);
			while(iss>>temp)
			{
				if(j==0)
				{
					t=temp;
					j=1;
				}
				else if(j==1)
				{
					c=temp;
					j=2;
				}
				else if(j==2)
				{
					f=temp;
					j=3;
				}
				else if(j==3)
				{
					x=temp;
					j=1;
					flag=2;
				}
				if(j==1 && flag==2)
				{
					double tim2=0.0,tim1=0.0,tim=0.0,r=2.0;
					while(1)
					{
						tim1=x/r+tim;
						tim2=x/(r+f)+c/r+tim;
						if(tim1<=tim2)
							break;
						else
						{
							tim+=c/r;
							r=r+f;
						}
					}
					fout<<fixed;
					fout.precision(7);
					fout<<"Case #"<<cnt++<<": "<<tim1<<endl;
				}
			}
		}
	}
	return 0;
}