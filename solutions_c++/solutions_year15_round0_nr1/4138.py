#include <iostream>
#include <fstream>
#include <string.h> 
using namespace std;
fstream fin,fout;
char str[10000];
int main()
{
	fin.open("in.cpp");
	fout.open("output.cpp");
	int t,n,ans;
	fin>>t;
	for(int i=1;i<=t;i++)
	{
		fin>>n;
		fin>>str;
		int sum=0;
		ans=0;
		for(int j=0;j<=n;j++)
		{
			sum+=str[j]-'0';
			if(sum<j+1)
			{
				sum++;
				ans+=1;
			}
		}
		fout<<"Case #"<<i<<": "<<ans<<endl;
	}
	
}
