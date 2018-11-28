/*
#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;
static char * month[]={"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November" , "December"};
int main()
{
	int t;
	scanf("%d",&t);
	getchar();
	for(int p=1;p<=t;p++)
	{
		char mo[10],temp;
		int d,y,m;
		scanf("%s %d %c %d",mo,&d,&temp,&y);
		for(int i=0;i<12;i++)
		{
			if(!strcmp(mo,month[i]))
			{
				m=i+1;
				break;
			}
		}
		
		
		char mo1[10],temp1;
		int d1,y1,m1;
		scanf("%s %d %c %d",mo1,&d1,&temp1,&y1);
		for(int i=0;i<12;i++)
		{
			if(!strcmp(mo1,month[i]))
			{
				m1=i+1;
				break;
			}
		}
		
		
		int cnt=0;
		
		if(y==y1)
		{
		
		
		if((m==2&&d<=29||m<2)&&(m1==2&&d1==29||m1>2))
		{
			if(y%4==0&&y%100!=0||y%400==0)
			{
			      cnt++;
			}
		}
		
		
		}
		else
		{
			for(int i=y+1;i<=y1-1;i++)
			{
				if(i%4==0&&i%100!=0||i%400==0)
			 	   cnt++;
			}
		
					
			if(y%4==0&&y%100!=0||y%400==0)
			{
			     if(m==2&&d<=29||m<2)
			        cnt++;
			
			
			if(y1%4==0&&y1%100!=0||y1%400==0)
			{
			     if(m1==2&&d1==29||m1>2)
			        cnt++;
			}
		
		}
		
		cout<<"Case #"<<p<<": "<<cnt<<endl;
		getchar();
	}
	return 0;
}
*/
#include<iostream>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include <bitset>
#include<algorithm>
using namespace std;


int main()
{
    
    int t,n,a[1001];
    cin>>t;
    for(int j=1;j<=t;j++)
    {
    	cin>>n;
    	for(int i=0;i<n;i++)
    	{
    		cin>>a[i];
    	}
    	int sum=0;
    	for(int i=0;i<n-1;i++)
    	{
    		if(a[i]>a[i+1])
    		   sum+=a[i]-a[i+1];
    	}
    	int sum1=0;
    	int cha=-1000;
    	for(int i=0;i<n-1;i++)
    	{
    		cha=max(cha,a[i]-a[i+1]);
    	}
    	 
    	for(int i=0;i<n-1;i++)
    	{
    		if(a[i]<=cha)
    			sum1+=a[i];
    		else
    		    sum1+=cha;
    	
    		
    	}
    	
    	cout<<"Case #"<<j<<": "<<sum<<" "<<sum1<<endl; 
    }
     
	return 0;
}
