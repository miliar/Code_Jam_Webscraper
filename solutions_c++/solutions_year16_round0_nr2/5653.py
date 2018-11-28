#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,j;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		string str;
		cin>>str;
		int l=str.length();
		if(l==1)
		{
			if(str[0]=='+')
			cout<<"Case #"<<i<<": 0\n";
			else if(str[0]=='-')
			cout<<"Case #"<<i<<": 1\n";
		}
		else
		{
			int flip=0;
			for(j=1;j<l;j++)
			{
				if(str[j]!=str[j-1])
				{
					flip++;
				}
			}
			if(str[l-1]=='-')
			flip++;
			cout<<"Case #"<<i<<": "<<flip<<endl;
		}
	}
	return 0;
 } 
