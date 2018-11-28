#include<bits/stdc++.h>
using namespace std;
typedef long long int longx;
int main()
{
	ifstream fin("cj_input.txt");
	ofstream fout("cj_output");
	longx T,N,res,count=0;
	string str;
	fin>>T;
	for(longx j=1;j<=T;j++)
	{
		fin>>N>>str;
		res=0;
		count=str[0]-'0';
		
		for(longx i=1;i<N+1;i++)
		{
			if(count<i)
			{
				res+=i-count;
				count=i;
			}
			count+=str[i]-'0';
		}
		fout<<"Case #"<<j<<": "<<res<<endl;
	}
}
