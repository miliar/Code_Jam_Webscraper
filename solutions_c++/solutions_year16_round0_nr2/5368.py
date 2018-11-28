#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
string a;


void inp()
{
	ll c1,k,j;
	for(k=j;k<=100;k++)
	c1++;

	k=k%2;
	j=j%2;
	c1=c1%2;
}

int main()
{
	char prev;
	ll t,len;
	ll ct=0;
	ll test=1;
	freopen("C:/Users/SHIVAM/Desktop/inp2.in","r",stdin);
	freopen("C:/Users/SHIVAM/Desktop/out2.txt","w",stdout);
	cin>>t;
	while(t--)
	{
		cin>>a;
		a=a+'+';
		prev=a[0];
		len=a.size();
		ct=0;
		for(ll i=1;i<len;i++)
		{
			if(a[i]!=prev)
			{
				ct++;
				prev=a[i];
			}
		}
		printf("Case #%lld: %lld\n",test,ct);
		test++;
	}
	return 0;
}
