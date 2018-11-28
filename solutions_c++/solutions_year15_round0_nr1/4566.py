#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
ifstream cin("A-large.in.txt");
ofstream cout("out.txt");

int main()
{
	int t,n,i,k,sum,ans,caseNum=0;
	char s[1005];

	cin>>t;
	while (t--)
	{
		caseNum++;
		cin>>n;
		cin>>s;
		sum=0;
		ans=0;
		for (i=0;i<=n;i++)
		{
			k=s[i]-'0';
			if (k==0) 
			{
				sum+=k;
				continue;
			}
			if (sum+ans>=i) 
			{
				sum+=k;
				continue;
			}
			ans=i-sum;
			sum+=k;
		}
		cout<<"Case #"<<caseNum<<": "<<ans<<endl;
	}
	return 0;
}