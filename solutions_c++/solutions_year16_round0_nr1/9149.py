#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out2.out","w",stdout);
	int t,i,n,done,p,j,count=1;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n;
		done=0;
		int a[]={0,0,0,0,0,0,0,0,0,0};
		if(n==0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
		count=1;
		p=n;
		while(done!=1)
		{
			while(p>0)
			{
				if(a[p%10]==0)
				   a[p%10]=1;
				   p=p/10;
			}
			done=1;
			for(j=0;j<10;j++)
			{
				if(a[j]==0)
				{
					done=0;
					break;
				}
			}
			count++;
			p=count*n;
			if(done==1)
			p=(p-n);
			//cout<<n<<endl;
		}
		/*for(int x=0;x<10;++x)
			cout<<a[x]<<" ";*/
			n=p;
		cout<<"Case #"<<i<<": "<<n<<endl;
	    }
	}
}
