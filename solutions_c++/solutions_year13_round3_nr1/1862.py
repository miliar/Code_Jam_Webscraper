#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
#include<utility>
#include<numeric>

using namespace std;

ifstream fin("data_in.txt");
ofstream fout("data_out.txt");

bool isVowel(char c)
{
	return c=='a'||c=='e'||c=='i'||c=='o'||c=='u';
}

static int dp[1000000+1];

int main()
{
	int T;
	fin>>T;
	string name;
	int n;
	for(int t=1;t<=T;++t)
	{
		fout<<"Case #"<<t<<": ";
		fin>>name>>n;
		bool isCons=false;
		int consLen=0;
		dp[name.length()]=0;
		for(int i=name.length()-1;i>=0;--i)
		{
			if(isVowel(name[i]))
			{
				dp[i]=dp[i+1];
				if(isCons)
				{
					isCons=false;
					consLen=0;
				}
			}
			else
			{
				if(isCons)
					++consLen;
				else
				{
					isCons=true;
					consLen=1;
				}
				if(consLen<n)
					dp[i]=dp[i+1];
				else
				{
					dp[i]=name.length()-(i+n)+1;
				}
			}
		}
		fout<<accumulate(dp,dp+name.length(),0)<<endl;
	}
}