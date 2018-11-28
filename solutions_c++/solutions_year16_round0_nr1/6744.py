#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("abc2.in","r",stdin);
	freopen("out2.txt","w",stdout);
	int t,i=1,arr[10]={0},sum=0;
	long long int n,p,m=1,k,l;
	cin>>t;
	while(i<=t)
	{
		for(int j=0;j<10;j++)
		arr[j]=0;
		
		sum=0;
		m=1;
		cin>>n;
		if(n==0){
		cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		i++;
		}
		
		else
		{
			while(1)
			{
								
				p=m*n;
				k=p;
				while(p>0)
				{
					l=p%10;
					if(arr[l]==0)
					{
						arr[l]=1;
						sum+=1;
						if(sum==10)
						{
							cout<<"Case #"<<i<<": "<<k<<endl;
							i++;
							break;
						}
					}
					p=p/10;
				}
				if(sum==10)
						{
							break;
						}
				
				m++;
			}
		}
	}
}
