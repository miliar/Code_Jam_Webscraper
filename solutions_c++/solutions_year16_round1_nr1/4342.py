#include<iostream>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int j;
	for(j=1;j<=t;j++)
	{
		string s,n="";
		char c;
		cin>>s;
		int i;
		c=s[0];
		n=n+c;
		for(i=1;i<s.size();i++)
			{
				if(s[i]>=c)
					n=s[i]+n;
				else
					n=n+s[i];
				c=n[0];
			}
		cout<<"Case #"<<j<<": "<<n<<"\n";


	}
}