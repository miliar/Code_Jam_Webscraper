#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	ll t,num=0;
	cin>>t;
	while(t--)
	{
	num++;
	ll spec,count=0,ans=0,i=1,p;
	cin>>spec;
	string a;
	cin>>a;
	p=a.length();
	while(i<p)
	{
		ans=ans+int(a[i-1])-48;
		if(ans<i)
		{
		count=count+(i-ans);
		ans=i;
		}
		i++;
	}
	cout<<"Case #"<<num<<": "<<count<<endl;
	
	}
	fclose(stdout);
	return 0;
}


