#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,i,j,s,extra,tot;
	cin>>t;
	string a;
	for(j=1;j<=t;j++)
	{
		tot=extra=0;
		cin>>s>>a;
		for(i=0;i<s+1;i++)
		{
			int x=a[i]-48;
			if(tot<i&&x!=0)
			{
				extra+=i-tot;
				tot+=extra;
			}
			tot+=x;
			if(tot>=9)
				break;
		}
		cout<<"Case #"<<j<<": "<<extra<<"\n";
	}

}