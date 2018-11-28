#include<bits/stdc++.h>
using namespace std;
int main()
{
		freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
	
	int t,i=1;
	string s;
	cin>>t;
	while(t--)
	{
		cin>>s;
		int l=s.length();
		for(int j=0;j<l;j++)
		{
			if(s[0]<=s[j])
			{
				for(int k=j;k>0;k--)
				{
					char temp=s[k];
					s[k]=s[k-1];
					s[k-1]=temp;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<s<<endl;
		i++;
	}
	return 0;
}
