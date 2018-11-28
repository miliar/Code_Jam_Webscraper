#include<bits/stdc++.h>
using namespace std;
int main()
{
	ifstream fin("inepuet.in");
	ofstream fout("Inpeuet.out");
	int t,sum,x,ans,caseno=1;
	string st;
	fin>>t;
	while(t--)
	{
		sum=ans=0;
		fin>>x;
		fin>>st;
		for(int i=0;i<=x;i++)
		{
			if(i-sum>0)
			{
				ans=ans+(i-sum);
				sum=sum+(i-sum);
			}
			else ans+=0;
			sum=sum+(st[i]-'0');
		}
		fout<<"Case #"<<caseno<<": "<<ans<<"\n";
		caseno++;
	}
	return 0;
}
