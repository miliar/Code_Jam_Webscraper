#include<iostream>
#include<iomanip>
#include<math.h>
#include<string>
#include<stdlib.h>
#include<algorithm>
using namespace std;

int main()
{
	int T;
	string S[102];
	int out[102];
	int Smax[102];
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		cin>>Smax[i];
		cin>>std::ws;
		getline(cin,S[i]);
	}
	for(int i=1; i<=T; i++)
	{
		int shycount = 0;
		int minppl = 0;
		for (int l = 0; l < Smax[i]+1; l++)
		{
			if((S[i][l]-'0')==0)
				continue;
			else if(shycount>=l)
			{
				shycount+=(S[i][l]-'0');
				continue;
			}
			else
			{
				minppl+=l-shycount;
				shycount=l+(S[i][l]-'0');
			}
		}
		out[i]=minppl;
	}
	for (int i = 1; i <= T; i++)
	{
		cout<<"Case #"<<(i)<<": "<<out[i]<<"\n";
	}
	return 0;
}
