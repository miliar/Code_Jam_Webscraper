#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	ifstream fin ("A-small-attempt0.in");
	ofstream fout ("A-small-attempt0.out");
	
	int t,r,f[17],s,si,k,i,j,a;
	
	fin>>t;
	
	for(k=1;k<=t;k++)
	{
		for(i=0;i<17;i++)
		f[i]=0;
		
		fin>>r;
		
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				fin>>a;
				
				if(i==r)
				f[a]++;
			}
		}
		
		s=si=0;
		fin>>r;
		
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				fin>>a;
				
				if(i==r && f[a])
				{
					s+=a;
					si++;
				}
			}
		}
		
		fout<<"Case #"<<k<<": ";
		
		if(!si)
		fout<<"Volunteer cheated!";
		else if(si==1)
		fout<<s;
		else
		fout<<"Bad magician!";
		
		fout<<endl;
	}
	
	return 0;
}

