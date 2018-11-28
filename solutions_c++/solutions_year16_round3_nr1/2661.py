#include<bits/stdc++.h>
using namespace std;
	struct par
	{
		int data;
		char m;
	};
bool acompare(par lhs, par rhs) { return lhs.data > rhs.data; }

int main()
{	

    freopen("A-large.in","r",stdin);
    freopen("out30.out","w",stdout);
	int z;
	cin>>z;
	for(int i=1;i<=z;i++)
	{	
		char k='A';
		int n,flag=0;
		cin>>n;
		par p[n];
		for(int j=0;j<n;j++)
		{	cin>>p[j].data;
			p[j].m=k;
			k++;
		}
		 std::sort(p, p+n , acompare);
		 cout<<"Case #"<<i<<": ";
		while(!flag)
		{	int sum=0;
			for(int j=0;j<n;j++)
			sum+=p[j].data;
			if(sum==0)	
			break;
			if(p[0].data==p[1].data)
			{
				if(p[0].data==p[2].data)	{	p[0].data--; cout<<p[0].m<<" "; }
				else
				{
					p[0].data--; cout<<p[0].m;
					p[1].data--; cout<<p[1].m<<" ";
				}
				
			}
			else
			{
					p[0].data--; cout<<p[0].m<<" ";
			}
			 std::sort(p, p+n , acompare);
		}
		cout<<endl;
		
	}
	return 0;
}
