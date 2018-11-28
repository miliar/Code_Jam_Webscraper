#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int r,r1,cnt=0,temp,temp1;
		bool a[17];
		for(int j=0;j<=16;j++)
		 a[j]=false;
		cin>>r;
		for(int j=0;j<4;j++)
		 for(int k=0;k<4;k++)
		{
			cin>>temp;
			if(j==r-1)
			  a[temp]=true;
		}
		cin>>r1;
		for(int j=0;j<4;j++)
		{ 
		 for(int k=0;k<4;k++)
		{
			cin>>temp;
			if(j==r1-1)
			{
				if(a[temp]==true)
				{ 
				 cnt++;
				 temp1=temp;
			    }
			}
			  
		}
	    }
	    cout<<"Case #"<<i+1<<": ";
	    if(cnt==0)
	    cout<<"Volunteer cheated!\n";
	    else if(cnt>1)
	    cout<<"Bad magician!\n";
	    else
	    cout<<temp1<<"\n";	 
	}
	
	return 0;
}

