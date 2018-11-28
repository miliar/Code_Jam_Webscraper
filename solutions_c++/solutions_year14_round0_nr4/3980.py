#include<iostream>
#include<algorithm>
#include<iomanip>
#define MIN 2
using namespace std;
int main()
{
	int t,i,j,ctr,k,k1,k2,point,score,n,idx;
	double a[1000],b[1000],x,min;
	cout<<fixed<<setprecision(7);
	
	cin>>t;
	
	for(i=1;i<=t;i++)
	{
		cin>>n;
		
		for(j=0;j<n;j++)
		{
			cin>>a[j];
		}
		for(j=0;j<n;j++)
		{
			cin>>b[j];
		}
		
		sort(a,a+n);
		sort(b,b+n);
		
		ctr=n-1;
		k1=n-1;
		k2=0;
		point=0;
		while(k1>=k2)
		{
			if(a[k1]>b[ctr])
			{
				point++;
				k1--;
				ctr--;
			}
			else
			{
				k2++;
				ctr--;
			}
		}
		
		ctr=n-1;
		score=0;
		k=0;
		while(ctr>=0)
		{
			x=a[ctr];
			
			min=MIN;
			
			for(j=0;j<n;j++)
			{
				if(b[j]==MIN)
				{
					
				}
				else
				if(b[j]>x)
				{
					if(b[j]<min)
					{
						min=b[j];
						idx=j;
					}
				}
			}
			
			if(min!=MIN)
			{
				b[idx]=MIN;	
			}
			else
			{
				b[k]=MIN;
				k++;
				score++;
			}
			ctr--;
		}
		
		cout<<"Case #"<<i<<": "<<point<<" "<<score<<"\n";
		
	}
	
	return 0;
}