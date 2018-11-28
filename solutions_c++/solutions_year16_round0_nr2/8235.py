#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int t1=1;t1<=t;t1++)
	{
		string s;
		cin>>s;
		int n=s.length();
		int flip=0;
		for(int i=0;i<n;i++)
		{
			if(s[i]=='-')
			{
				if(i!=0)
				{
					flip++;
				}
				while(i+1!=n&&s[i+1]=='-')
				{
					i++;
				}
				flip++;
			}
		}
		cout<<"Case #"<<t1<<": "<<flip<<endl;
	}
}
