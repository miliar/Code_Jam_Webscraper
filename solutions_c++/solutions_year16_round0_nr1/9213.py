#include<bits/stdc++.h>
using namespace std;
int main()
{	
 freopen("A-large.in","r",stdin);
	freopen("out3.out","w",stdout);
	int t,i,n,flag,p,j,cc=1;
	cin>>t;
	for(i=1;i<=t;i++)
	{	cin>>n;
		flag=0;
		int arr[]={0,0,0,0,0,0,0,0,0,0};
		if(n==0)
		{	cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
		cc=1;
		p=n;
		while(flag!=1)
		{	while(p>0)
			{	if(arr[p%10]==0)
				   arr[p%10]=1;
				   p=p/10;
			}
			flag=1;
			for(j=0;j<10;j++)
			{	if(arr[j]==0)
				{	flag=0;
					break;
				}
			}
			cc++;
			p=cc*n;
			if(flag==1)
			p=(p-n);
		}
		n=p;
		cout<<"Case #"<<i<<": "<<n<<endl;
	    }
	}
}
