#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	fstream fin,fout;
	fin.open("opo2.in",fstream::in);
	fout.open("out2.txt",fstream::out);
	int T,i,ai;
	string x,y,temp;
	ai=1;
	fin>>T;
	while(T--)
	{
		
		fin>>x;
		y=x.substr(0,1);
		for(i=1;i<x.length();i++)
		{
			if(x[i]>=y[0])y=x[i]+y;
			else y+=x[i];
		}
		fout<<"Case #"<<ai<<": "<<y<<endl;
		ai++;
	}

	
	
	fin.close();
	fout.close();
	return 0;
}
