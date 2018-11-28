#include<iostream>
#include<fstream>
using namespace std;

int nd[10],ans;


void tally(long long int num)
{
	long long int p,q;
	p=num;
	while(p>0)
	{
		q=p%10;
		nd[q]++;
		p=p/10;
	}
	
}
bool check()
{
	int i;
	for(i=0;i<10;i++)
	{
		if(nd[i]==0)
		return false;
	}
	return true;
}




int main()
{
	
	fstream fin,fout;
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);
	
	int i,t;
	fin>>t;
	for(i=1;i<=t;i++)
	{
		for(int k=0;k<10;k++)
		nd[k]=0;
		long long int num,temp=0;
		fin>>num;
		int j=1;
		while(j<100)
		{
			temp=temp+num;
			tally(temp);
			if(check())
			break;
			j++;
		}
		
		if(j==100)
		fout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		else
		fout<<"Case #"<<i<<": "<<temp<<endl;
	}
	cout<<"done";
	return 0;
}
