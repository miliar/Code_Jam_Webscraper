#include<iostream>
using namespace std;
int main()
{
	int t,t1;
	cin>>t;
	for(t1=1; t1<=t; t1++)
	{
		int n,i;
		cin>>n;
		int p[n],tot=0;
		int maxi,max,max2,max2i;
		int temp,temp2;
		for(i=0; i<n; i++)
		{
			cin>>p[i];
			tot+=p[i];
		}
		cout<<"Case #"<<t1<<": ";
		while(tot>0)
		{
			if(tot==3)
			{
				int flag=0;
				for(i=0; i<n; i++)
				{
					if(p[i]>1)
					{
						flag=1;
						break;
					}
				}
				if(flag==0)
				{
					for(i=0; i<n; i++)
					{
						if(p[i]==1)
						{
							p[i]--;
							char t=65+i;
							cout<<t<<" ";							
							break;
						}
					}
					tot--;
					continue;
				}
			}
			max=p[0];  maxi=0;
			max2=-1;   max2i=-1;
			for(i=1; i<n; i++)
			{
				if(p[i]>max2)
				{
					max2=p[i];  max2i=i;
					if(max2>max)
					{
						temp=max;
						max=max2;
						max2=temp;
						temp2=maxi;
						maxi=max2i;
						max2i=temp2;
					}
				}
			}
			char t1=65+maxi,t2=65+max2i;
			cout<<t1<<t2<<" ";
			p[maxi]--; p[max2i]--;
			tot-=2;
		}
		cout<<"\n";
	}
}
