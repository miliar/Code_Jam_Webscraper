#include<bits/stdc++.h>
using namespace std;
int max(int *a,int d)
{
	int i,j,k;
	k=-1;j=0;
	for(i=0;i<d;i++)
	{
		if(a[i]>k)
		{
			j=i;
			k=a[i];
		}
	}
	return j;
}
int main()
{
	freopen("D-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	long long int t,y=1;
	cin>>t;
	while(t--)
	{
		long long int x,r,c,i,gabriel=0,richard=0,j,k,l,m,n=3,o,p=4;
		cin>>x>>r>>c;
		if(x==4)
		{
			if(r==p&&c==p||r==n&&c==p||r==4&&c==3)
	              gabriel=1;
	          else 
	              richard=1;
		}
		else if(x==3)
		{
			   if(r==1||c==1)
	                    richard=1;
	                else if(r==3||c==3)
	                    gabriel=1;
	                else
	                    richard=1;
		}
		else if(x==2)
		{
			if(r==1&&c==3||r==1&&c==1||r==3&&c==3||r==3&&c==1)
	              richard=1;
	          else
	              gabriel=1;
		}
		else
		{
			gabriel=1;
		}
		//cout<<i<<endl;
	//cout<<count[a[i]]<<endl;
	//	i = i - count[a[i]]+1;
		//cout<<i<<endl;
		//cout<<ans<<endl;
		//cout<<cmp<<endl;
		//cout<<i<<endl;
	
		if(gabriel==1)
		cout<<"Case"<<" "<<"#"<<y<<":"<<" "<<"GABRIEL"<<endl;
		else
		cout<<"Case"<<" "<<"#"<<y<<":"<<" "<<"RICHARD"<<endl;
		y++;

	}
}
