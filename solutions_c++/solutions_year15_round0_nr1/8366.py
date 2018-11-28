#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int t;ofstream fout;fout.open("./output.txt");
	ifstream fin;fin.open("./input.txt");
	fin>>t;int p=1;
	while(t--)
	{
		int *a;
		int smax;
		fin>>smax;
		cout<<smax;
		a=new int[smax+1];
		string s;
		fin>>s;
		a[0]=0;int count=0;
		for(int i=1;i<=smax;i++)
		{
			a[i]=a[i-1]+(s[i-1]-48);
		}
		
		for(int i=0;i<smax+1;i++)
		{
			if(a[i]>=i);
			else
			if(a[i]<i&&(s[i]-48==0));
			else
			{
				int p=i-a[i];
				count+=p;
				for(int j=i;j<smax+1;j++)
					a[j]+=p;
				
			}
				
		}	
			fout<<"case #"<<p<<": "<<count<<"\n";
			p++;
	}
}
