#include<bits/stdc++.h>
using namespace std;
long long m[20];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	long long a,b,c,d,e,num;
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin>>a;
	for(b=0;b<a;b++)
	{
		cin>>c;
		memset(m,0,sizeof(m));
		cout<<"Case #"<<b+1<<": "; 
		if(c==0)cout<<"INSOMNIA\n";
		else 
		{
			num=10;
			d=1;
			while(num)
			{
				e=c*d;
				while(e)
				{
					m[e%10]++;
					if(m[e%10]==1)num--;
					e/=10;
				}
				d++;
			}
			cout<<(d-1)*c<<"\n";
		}
	}
}
