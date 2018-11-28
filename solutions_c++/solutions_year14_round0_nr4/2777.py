#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	int n,i,j,k,score1,score2,sc1,sc2;
	double x;
	int a[1200],b[1200],flag;
	double v1[1200],v2[1200];
	cin>>t;k=0;
	while(t--)
	{
		cin>>n;k++;
		for(i=0;i<n;i++)
		{
			cin>>v1[i];
		}
		for(i=0;i<n;i++)
		{	
			cin>>v2[i];
		}
		sort(v1,v1+n);
		sort(v2,v2+n);
		score1=0;score2=0;sc1=0;sc2=0;
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=0;i<n;i++)
		{
			flag=0;
			for(j=0;j<n;j++)
			{
				if(b[j]==0 && v2[j]>v1[i])
				{
					//cout<<v2[j]<<" "<<v1[i]<<"\n";
					b[j]=1;
					flag=1;break;
				}
			}
			if(flag==0){score2++;}
		}
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(i=0;i<n;i++)
		{
			flag=0;
			for(j=n-1;j>=0;j--)
			{
				if(b[j]==0 && v2[j]>v1[i])
				{
					//cout<<v1[i]<<" "<<v2[j]<<"\n";
					b[j]=1;
					flag=1;break;
				}
			}
			if(flag==0){sc1++;}
			flag=0;
			
			for(j=0;j<n;j++)
			{
				if(a[j]==0 && v2[j]<v1[i])
				{
					a[j]=1;
					flag=1;break;
				}
			}
			if(flag==1){sc2++;}
			flag=0;
					
			
		}	
		score1=max(sc1,sc2);
		printf("Case #%d: %d %d\n",k,score1,score2);
	}
	return 0;
}
					
					
					
					
					
					
					
