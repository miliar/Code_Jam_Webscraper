#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int val,t,i;
	string s,k,l,pre,vala;
	cin>>t;
	val=0;
	while(t--)
	{
		val++;
		cin>>s;
		k=k+s[0];
		for(i=1;i<s.length();i++)
		{
			
			l=s[i];
			vala=k[0];
			if(vala.compare(l)<=0)
			{
				k.insert(0,l);
			}
			else
			{
				k.insert(i,l);
			}
			
		}
		cout<<"Case #"<<val<<": ";
		
		cout<<k<<endl;
		k.clear();
	}
	return 0;
}