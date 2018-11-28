#include<bits/stdc++.h>
using namespace std;

ifstream goo;
ofstream gle;

bool tab[100];

void solve()
{
	unsigned long long a,l,c,d;
	int b=0;
	for(int i=0; i<=9; i++) tab[i]=0;
	goo>>a;
	l=a;
	if(a==0)
	{
		gle<<"INSOMNIA\n";
		return;
	}
	while(true)
	{
		c=a;
		while(c>0)
		{
			d=c-(c/10)*10;
			if(tab[d]==0)
			{
				tab[d]=1;
				b++;
			}
			c/=10;
		}
		if(b==10) break;
		a+=l;
	}
	gle<<a<<"\n";
}

int main()
{
	int t;
	ios_base::sync_with_stdio(0);
   	goo.open("C:\\Users\\Mateusz\\Downloads\\A-large.in");
   	//goo.open("C:\\Users\\Mateusz\\Desktop\\goo.in");
   	gle.open("C:\\Users\\Mateusz\\Desktop\\gle.out");
	goo>>t;
	for(int i=1; i<=t; i++)
	{
		gle<<"Case #"<<i<<": ";
		solve();
	}
	goo.close();
	gle.close();
	return 0;
}
