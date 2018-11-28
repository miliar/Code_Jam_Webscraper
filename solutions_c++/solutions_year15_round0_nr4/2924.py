/*
	Manish Kumar
	c0dezer0
	www.fb.com/kur.manish
*/
#include <bits/stdc++.h>
#define mod 1000000007
 
using namespace std;

int solve()
{
	
	int v,r,c;
	cin>>v>>r>>c;
	if(v>=7)
		return 0;
	if(v==1)
		return 1;
	int maxi= max(c,r);
	if(v>maxi)
		return 0;
	if((r*c)%v!=0)
		return 0;
	if(v==2)
		return 1 ;

	if(r>c)
	swap (r,c);
	for(int i=1;i<=v;i++)
	{
			int a=i;
			if(a>r && a>c)
				return 0;
			int b=v/i;
			if(a>b)
			swap(a,b);
			if(a<=r && b<=c)
				continue;
			return 0;
	}
	int rem=0;
	if(v>r)
		rem=v-r;
	if(v>(r) && (rem+1)>r)
		return 0;
	for(int i=1;i<=rem;i++)
	{
		for(int l=0;l<=i;l++)
		{
			int rt=i-l;
			if(l==0 || (l+1+rt)<r)
				continue;
			else
			{
				if((l+v)%r!=0)
					return 0;
			}
			if(rt==0)
				continue;
			else
			{
				if((rt+v)%r!=0)
					return 0;
			}		
		}
	}
	rem=0;
	if(v>c)
	rem=v-c;
	for(int i=1;i<=rem;i++)
	{
		for(int l=0;l<=i;l++)
		{
			int rt=i-l;
			if(l==0 || (l+1+rt)<c)
				continue;
			else
			{
				if((l+v)%c!=0)
					return 1;
			}
			if(rt==0)
				continue;
			else
			{
				if((rt+v)%c!=0)
					return 1;
			}		
		}
	}
	return 1;
}



int main() 
{
	int test;
	cin>>test;
	for(int i=1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		cout<<(solve()?"GABRIEL":"RICHARD");
		cout<<endl;
	}
	return 0;
}
