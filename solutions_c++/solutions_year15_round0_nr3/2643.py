#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back

//0-'1',1-'i',2-'j',3-'k',4-'-1',5-'-i',6-'-j',7-'-k'

int main()
{
	freopen("ip.txt","r",stdin);
	freopen("op.txt","w",stdout);
	bool ok1,ok2;
	ll prod[4][8] =
	{
		{0,1,2,3,4,5,6,7},
		{1,4,3,6,5,0,7,2},
		{2,7,4,1,6,3,0,5},
		{3,2,5,4,7,6,1,0},
	};
	
	map<char,ll> m;
	m['i'] = 1,m['j'] = 2,m['k'] = 3;
	
	ll t,n,x,i,v,j,c;
	cin>>t;
	string s,s1;
	
	c = 1;
	
	while(t--)
	{
		cin>>n>>x;
		cin>>s;
		cout<<"Case #"<<c++<<": ";
		s1 = "";
		for(i=0;i<x;i++)s1+=s;
		n*=x;
		v = prod[m[s1[0]]][0];
		for(i=1;i<n;i++)
		{
			v = prod[m[s1[i]]][v];
			v = (v+4)%8;
		}
		
		if(v==0)
		{
			ok1 = false;
			
			v = prod[m[s1[0]]][0];
			for(i=1;i<n;i++)
			{
				if(v==1)
				{
					ok1 = true;
					break;
				}
				v = prod[m[s1[i]]][v];
				v = (v+4)%8;
			}
			i--;
			ok2 = false;
			
			v = prod[m[s1[n-1]]][0];
			for(j=n-2;j>=0;j--)
			{
				if(v==3)
				{
					ok2 = true;
					break;
				}
				if(v<4)
				{
					v = prod[v][m[s1[j]]];
				}
				else
				{
					v = ((prod[v-4][m[s1[j]]])+4)%8;
				}
				v = (v+4)%8;
			}
			j++;
			
			
			if(ok1 && ok2 && j>i)
			{
				cout<<"YES\n";
			}
			else
			{
				cout<<"NO\n";
			}
		}
		else
		{
			cout<<"NO\n";
		}
		
	}
	
    return 0;
}

