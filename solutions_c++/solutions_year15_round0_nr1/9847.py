#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,i,j,res,standing,m;
	string s;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>m>>s;
		res = 0;
		standing = 0;
		for(j=0;j<m+1;j++)
		{
			if(standing<j)
			{
				res+=j-standing;
				standing = j;
			}
			standing += s[j]-'0';
		}
		cout<<"Case #"<<i<<": "<<res<<endl;
	}
	return 0;
}
