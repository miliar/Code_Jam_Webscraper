#include<bits/stdc++.h>
using namespace std;
	struct par
	{
		int data;
		char x;
	};
bool acompare(par lhs, par rhs) { return lhs.data > rhs.data; }

int main()
{	

    freopen("A-large.in","r",stdin);
    freopen("outyee.out","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{	
		char k='A';
		int n,done=0;
		cin>>n;
		par p[n];
		for(int j=0;j<n;j++)
		{	cin>>p[j].data;
			p[j].x=k;
			k++;
		}
		 std::sort(p, p+n , acompare);
		 cout<<"Case #"<<i<<": ";
	//	for(int j=0;j<n;j++)
	//		cout<<p[j].data<<" "<<p[j].x<<endl;
		while(!done)
		{	int sum=0;
			for(int j=0;j<n;j++)
				sum+=p[j].data;
			if(sum==0)	break;
			if(p[0].data==p[1].data)
			{
				if(p[0].data==p[2].data)	{	p[0].data--; cout<<p[0].x<<" "; }
				else
				{
					p[0].data--; cout<<p[0].x;
					p[1].data--; cout<<p[1].x<<" ";
				}
				
			}
			else
			{
					p[0].data--; cout<<p[0].x<<" ";
			}
			 std::sort(p, p+n , acompare);
		}
		cout<<endl;
		
	}
	return 0;
}
