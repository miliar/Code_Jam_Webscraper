#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,s,i;
	char st[2000];
	cin>>t;
	for(int tc=1;tc<=t;tc++)
	{
		cin>>s;
		cin>>st;
		int tot=0;
		int add=0;
		for(i=0;i<=s;i++)
		{
			st[i]-='0';
			if(tot<i)
			{
				add+=(i-tot);
				tot=(i+st[i]);
			}
			else tot+=st[i];
		}
		cout<<"Case #"<<tc<<": "<<add<<endl;
	}
}
