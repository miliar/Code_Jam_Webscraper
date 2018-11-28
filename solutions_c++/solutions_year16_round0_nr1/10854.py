#include<bits/stdc++.h>
using namespace std;
int main()
{
	long long int t,n,i,j,ii,c,count;
	//freopen("1.txt","r",stdin);
	//freopen("2.txt","w",stdout);
	cin>>t;
	int a[10];
	for(ii=1;ii<=t;ii++)
	{
		cin>>n;
		int f=0;
		c=0;
		memset(a,0,sizeof(a));
		for(i=1;i<=100;i++)
		{
			j=i*n;
			while(j>0)
			{
				int dig=j%10;
				if(a[dig]==0)
				{
					a[dig]=1;
					c++;
				}
				if(c==10)
				{
				f=1;
				break;
			    }
			    j/=10;
			}
			if(f==1)
			{
			cout<<"Case #"<<ii<<": "<<i*n<<endl;
			break;
		   }
		   
		   		}
		   		if(f==0)
		   		{
		   		
		   
		   	cout<<"Case #"<<ii<<": "<<"INSOMNIA"<<endl;
		   	
		   

				   }
	}
}
