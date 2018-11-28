#include<iostream>
#include<stdio.h>
using namespace std;

int toint(char c)
{
	return ((int) c - 48);
}

int main()
{
	int T;
	freopen( "input.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int Smax;
		long peeps;
		long peepstoadd;
		char S[1002];
		cin>>Smax;
		cin>>S; //check!!
		peeps=toint(S[0]);
		peepstoadd=0;
		for(int j=1;j<=Smax;j++)
		{
			//cout<<j<<" "<<peeps<<endl;
			if(S[j]=='0')
			{
				continue;
			}
			if(j<=peeps)
			{
				peeps+=toint(S[j]);
			}
			else
			{
				int x=j-peeps;
				peepstoadd+=x;
				peeps+=x;
				peeps+=toint(S[j]);
			} 
		}
		cout<<"Case #"<<i+1<<": "<<peepstoadd<<endl; 
	}
}