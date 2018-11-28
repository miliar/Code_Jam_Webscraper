#include<bits/stdc++.h>
using namespace std;

ifstream goo;
ofstream gle;

void solve()
{
	unsigned long long a=1,b,c,n,m,d;
	vector<int> v;
	goo>>n>>m;
	//cout<<n;
	for(int i=1; i<n; i++) a*=2;
	//cout<<a;
	a++;
	while(m>0)
	{
		b=0;
		c=0;
		v.clear();
		for(int i=2; i<=10; i++)
		{
			b=0;
			d=1;
			for(int j=0; j<n; j++)
			{
				if(a&1<<j) b+=d;
				d*=i;
			}
			d=0;
			for(int j=2; j*j<=b; j++)
			{
				if(b%j==0)
				{
					v.push_back(j);
					d=1;
					break;
				}
			}
			if(d==0)
			{
				c=1;
				break;
			}
		}
		if(c==0)
		{
			for(int i=n-1; i>=0; i--)
			{
				if(a&1<<i) gle<<"1";
				else gle<<"0";
			}
			for(int i=0; i<v.size(); i++) gle<<" "<<v[i];
			gle<<"\n";
			m--;
		}
		a+=2;
	}
	return;
}

int main()
{
	int t;
	ios_base::sync_with_stdio(0);
   	goo.open("C:\\Users\\Mateusz\\Downloads\\C-small-attempt2.in");
   	//goo.open("C:\\Users\\Mateusz\\Desktop\\goo.in");
   	gle.open("C:\\Users\\Mateusz\\Desktop\\gle.out");
	goo>>t;
	for(int i=1; i<=t; i++)
	{
		gle<<"Case #"<<i<<":\n";
		solve();
	}
	goo.close();
	gle.close();
	return 0;
}
