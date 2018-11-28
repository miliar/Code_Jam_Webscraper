#include<iostream>
#include<fstream>
using namespace std;

string s,s1[100000];
long int p=0;


void after(string ss,long int i,long int n)
{
	if(i==n)
	s1[p++]=ss;

	else
	{
		
		after(ss+s[i],i+1,n);
		
		after(s[i]+ss,i+1,n);
		
	}
	
}

int main()
{
	long int i,j,k,n,t,l,q;
	
	string max,ss,sa,sa1;

		ofstream outfile;
  	outfile.open("E:\\codejam\\gcodeout.txt");

	
	cin>>t;
	q=1;
	while(t--)
	{
		cin>>s;
		
		ss="";
		
		p=0;
		for(i=0;i<100000;i++)
		s1[i]="";
		
		ss+=s[0];
		k=1;
		
		after(ss,k,s.length());
		
	//	for(i=0;i<p;i++)
	//	cout<<s1[i]<<endl;
		
		max=s1[0];
		
		for(i=1;i<p;i++)
		{
			sa1=s1[i];
			
			if(max<sa1)
			max=sa1;
			
			
		}
		
		outfile <<"Case #"<<q++<<":  " <<max<<endl;
		
	}
	
	
}
