#include<iostream>
using namespace std;
int main()
{
	float naomi[1000],ken[1000];
	int i,j,k,t,z[50],n,w[50],l,p,m;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n;
		for(j=0;j<n;j++)
		{
			cin>>naomi[j];
		}
		for(j=0;j<n;j++)
		{
			cin>>ken[j];
		}
		for(j=0;j<n;j++)
		{
			for(k=0;k<n;k++)
			{
				if(naomi[j]<naomi[k])
				{
					naomi[j]=naomi[j]+naomi[k];
					naomi[k]=naomi[j]-naomi[k];
					naomi[j]=naomi[j]-naomi[k];
				}
				if(ken[j]>ken[k])
				{
					ken[j]=ken[j]+ken[k];
					ken[k]=ken[j]-ken[k];
					ken[j]=ken[j]-ken[k];
				}
			}
			
		}
		z[i]=0;
		w[i]=0;
		l=n-1;
		for(j=0;j<n;j++)
		{
			if(naomi[l]>ken[j])
			{
				z[i]++;
				l--;
			}
			m=j;
			p=l;
			while(naomi[p]<ken[m])
			{
				p--;
				m++;
			}
			while(n==l)
			{
				p++;
				if(naomi[p]>ken[m])
				{
					z[i]++;
					
				}
			}
			

			
		}
	
		for(j=0;j<n;j++)
		{
			for(k=n-1;k>=0;k--)
			{
				if(naomi[j]<ken[k])
				{
					w[i]++;
					ken[k]=0;
					break;
				}
			}
		}
		w[i]=n-w[i];
		
		
	}
	for(i=0;i<t;i++)
	cout<<"Case #"<<(i+1)<<": "<<z[i]<<" "<<w[i]<<endl;
	
}
