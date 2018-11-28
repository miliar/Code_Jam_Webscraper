#include<bits/stdc++.h>
using namespace std;
int main()
{
	ifstream fin("cj_input.txt");
	ofstream fout("cj_output");
	int T,x,r,c,res;
	fin>>T;
	for(int k=1;k<=T;k++)
	{
		fin>>x>>r>>c;
		{
			if(x==1)
			res=1;
			else
			if(x==2)
			{
				if((r*c)%2==1)
				res=0;
				else
				res=1;
			}
			else
			if(x==3)
			{
				if((r*c)%3==0)
				{
					if((r<=1)||(c<=1))
					res=0;
					else
					res=1;
				}
				else
				res=0;
			}
			else
			if(x==4)
			{	
				if((r*c)%4==0)
				{
					if((r<=2)||(c<=2))
					res=0;
					else
					res=1;
				}
				else
				res=0;
			}
		}
		if(res)
		fout<<"Case #"<<k<<": GABRIEL\n";
		else
		fout<<"Case #"<<k<<": RICHARD\n";
	}
}
