#include<iostream>
#include<fstream>
using namespace std;




int main()
{
	
	fstream fin,fout;
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);
	
	int i,t;
	fin>>t;
	for(i=1;i<=t;i++)
	{
		int k,c,s,j;
		fin>>k>>c>>s;
		if(k==s)
		{
			fout<<"Case #"<<i<<": ";			
			for(j=1;j<=k;j++)
			fout<<j<<" ";
			fout<<endl;
		}
		else if((s==k-1)&&(c>1))
		{
			fout<<"Case #"<<i<<": ";			
			for(j=2;j<=k;j++)
			fout<<j<<" ";
			fout<<endl;
		}
		else
		{
			fout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;				
		}



	}
	cout<<"done";
	return 0;
}
