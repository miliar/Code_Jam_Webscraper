#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("out9000.out","w",stdout);
	int t;
	cin>>t;
	for(int x=1;x<=t;++x)
	{
		string s,a;
		cin>>s;
		int k=s.length(),i=1,last=1;
		a[0]=s[0];
		while(i<k)
		{
			if(s[i]>=a[0])
			{
				for(int j=last-1;j>=0;j--)
					a[j+1]=a[j];
				a[0]=s[i];
				last++;	
			}
			else
			{
				a[last++]=s[i];
			}
			i++;
		}
		cout<<"Case #"<<x<<": ";
		for(int i=0;i<last;++i)
			cout<<a[i];
		cout<<endl;
	}
}


