#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	fstream fin,fout;
	fin.open("bb.in",fstream::in);
	fout.open("out1.txt",fstream::out);
	string x;
	int T,i,o,ans;
	o=1;
	fin>>T;
	while(T--)
	{
		ans=0;
		i=0;
		fin>>x;
		
		while(i<x.length())
		{
			while(x[i]==x[i+1]&&(i+1)<x.length())i++;
			if(i>=(x.length()-1))
			{
				if(x[i]=='-')ans+=1;
			}
			else
			ans+=1;
			i++;	
		
		}
		
		fout<<"Case #"<<o<<": "<<ans<<endl;
		o++;
	}
	
	fin.close();
	fout.close();
	return 0;
}
