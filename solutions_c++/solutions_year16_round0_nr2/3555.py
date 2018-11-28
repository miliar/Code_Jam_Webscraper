#include<iostream>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("q2_l1.out","w",stdout);
	int t;
	cin>>t;
	int k=0;
	while(t--)
	{
		k++;
		string s;
		cin>>s;
		int l=s.length();
		int sg=0,ctr=1;
		char mt='+';
		int ans=0;
		if(s[0]=='+')
		{
			sg=1;
			mt='+';
		}
		else
		{
			sg=0;
			mt='-';
		}
		for(int i=1;i<l;i++)
		{
			if(s[i]!=mt)
			{
				mt=s[i];
				ctr++;
			}
		}
		if(sg==1)
		{
			ans=(ctr/2)*2;
		}
		else
		{
			if(ctr%2==0)
			{
				ctr--;
			}
			ans++;
			ans=ans+(ctr/2)*2;
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
