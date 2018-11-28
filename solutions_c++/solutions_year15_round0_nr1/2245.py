#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,i,j,k,total,friends;
	string s;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>k;
		cin>>s;
		total=friends=0;
		for(j=0;j<=k;j++)
		{
			if(total<j)
			{
				friends+=(j-total);
				total=j;
			}
			total+=(s[j]-'0');
		}
		cout<<"Case #"<<i<<": "<<friends<<endl;
	}
	return 0;
}
