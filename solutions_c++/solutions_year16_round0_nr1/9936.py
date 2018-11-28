#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("2.txt","w+",stdout);
	int n,m=1,a[14],q,t,i,j;
	long long p,r;
	cin>>t;
	while(t--)
	{
		cin>>n;
		memset(a,0,sizeof(a));
		r=0;
		if(n!=0)
		for(i=1;;i++)
		{
			for(j=0;j<10;j++)
			{
				if(a[j]!=1)
				break;
			}
			if(j==10)
			break;
			r=r+n;
			p=r;
			while(p)
			{
				q=p%10;
				p=p/10;
				a[q]=1;
			}
		}
		cout<<"Case #"<<m++<<": ";
		if(n==0)
		cout<<"INSOMNIA";
		else
		cout<<r;
		cout<<endl;
	}
	return 0;
}
		
			
			
		
