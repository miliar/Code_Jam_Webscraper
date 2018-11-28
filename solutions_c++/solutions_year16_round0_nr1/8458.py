#include<bits/stdc++.h>

using namespace std;
#define ll long long
#define DIG 10
#define SIZE 10000

void findDigs(ll r, set<int>& s)
{
	int dig  = 0;
	
	while(r)
	{
		dig = r %10;
		if( s.find(dig) == s.end() )	
		{
			s.insert(dig);
		}
		r /= 10;
	}
}
int main(void)
{
	int t,te;
	cin>>te;
	ll n,i,r;
	
	for(t=1;t <= te;t++)
	{		
		cin>>n;
		set<int> s;
		bool lastFound = false;
		for(i=1;i < SIZE; i++)			
		{
			r = i*n;
			findDigs(r,s);
			if( s.size() == DIG )
			{
				lastFound = true;
				break;
			}
		}
		printf("Case #%d: ",t);
		if( lastFound )
		{
			cout<<r<<endl;
		}
		else
		{
			cout<<"INSOMNIA\n";
		}
	}
	return 0;
}
