#include<iostream>
using namespace std;

int main()
{
	int t,n,i,j,k,dwar,nwar,max,min;
	float naomi[1000],ken[1000],temp;
	cin>>t;
	for(int p=0;p<t;p++)
	{   dwar=nwar=0;
		cin>>n;
		for(i=0;i<n;i++)
		 cin>>naomi[i];
		for(i=0;i<n;i++)
		 cin>>ken[i];
		for(i=0;i<n-1;i++)//naomi sorting in increasing order
		{
			for(j=i+1;j<n;j++)
			{
				if(naomi[i]>naomi[j])
				{
					temp=naomi[i];
					naomi[i]=naomi[j];
					naomi[j]=temp;
				}
			}
		}
		
		for(i=0;i<n-1;i++)//ken sorting in decreasing order
		{
			for(j=i+1;j<n;j++)
			{
				if(ken[i]<ken[j])
				{
					temp=ken[i];
					ken[i]=ken[j];
					ken[j]=temp;
				}
			}
		}
		
		max=0;
		min=n-1;
		for(i=0;i<n;i++)
		{
			if(naomi[i]<ken[min])
			{
				max++;
			}
			else
			{
				min--;
				dwar++;
			}
		}
		
		
		max=0;
		min=n-1;
		for(i=n-1;i>=0;i--)
		{
			if(naomi[i]>ken[max])
			{
				min--;
				nwar++;
			}
			else
			{
				for(j=0;j<n;j++)
				{
					if(ken[j]<naomi[i])
					 break;
				}
				for(k=j-1;k<min;k++)
				{
					ken[k]=ken[k+1];
				}
			}
		}
		cout<<"Case #"<<p+1<<": "<<dwar<<" "<<nwar<<endl;
	}
	
	return 0;
}
