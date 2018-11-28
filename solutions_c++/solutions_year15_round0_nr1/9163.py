#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<fstream>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("B.txt");

int T,n,A[1003];
char S[1003];
int main()
{
	fin>>T;
	for(int cs=1;cs<=T;cs++)
	{
		fin>>n>>S;
		for(int i=0;i<=n;i++)A[i]=(int)(S[i]-'0');
		
		int res=0;
		for(int x,i=1;i<=n;i++)
		{
			A[i]+=A[i-1];
			if(S[i]!='0')
			{
				x=i-A[i-1];
				if(x>0)
				{
					A[i]+=x;
					res+=x;
				}			
			}
		}
		fout<<"Case #"<<cs<<": "<<res<<"\n";
	}
	return 0;
}
