# include<fstream.h>
#include<iostream.h>
int mn,z,i,r,c,x;
ifstream fin;
ofstream fout;
void resultg()
{
	fout<<"Case #"<<z<<": GABRIEL\n";
}
void resultr()
{
	fout<<"Case #"<<z<<": RICHARD\n";
}
void main()
{
	fin.open("m.in");
	fout.open("n.txt");
	fin>>mn;
	cout<<mn;//
	for(z=1;z<=mn;z++)
	{
		fin>>x;
		fin>>r;
		fin>>c;
		cout<<x<<" "<<r<<" "<<c<<"\n";
		if((r*c)%x!=0)
		{
			resultr();
		}
		else
		{
			if(x==1||x==2)
			{
				resultg();
			}
			else if(x==3)
			{
				if((r==1)||( c==1))
				{
				resultr();
				}
				else
				{
					resultg();
				}
			}
			else if(x==4)
			{
				if((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4))
				{
					resultg();
				}
				else
				{
					resultr();
				}
			}
		}
	}
}