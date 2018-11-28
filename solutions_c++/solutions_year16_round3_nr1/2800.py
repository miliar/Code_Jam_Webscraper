#include<iostream>
#include<bits/stdc++.h> 
#include<fstream>
#include<set>
#include<map>
#define up(j,n,i) for(i=j;i<n;i++)
using namespace std;
typedef long long int lld;
fstream I,O;
lld check(lld k,lld * sum,lld n,lld *a)
{
//cout<<"this is check"<<k<<' '<<*sum<<' '<<n<<endl;
	lld i=0,j,cnt=0,temp,cnt2=0,ptemp;
	up(0,n,i)
	{
	
		cnt=0;
		temp=*sum;
		if(a[i]>0)
		{a[i]--;cnt=1;}
		else
		continue;
		temp--;
		//cout<<i<<'-'<<a[i]<<' ';
		up(0,i+1,j)
		{
			cnt2=0;	
			if(i!=j)
			{
				
				if(a[j]>0)
				{a[j]--;cnt2=1;}
				else
				{
				continue;
				}
				temp--;
			}
			
			
				//cout<<j<<'-'<<a[j]<<endl;
				
			ptemp=temp;
			temp/=2;
			bool flag=0;
			lld k=0;
			for(k=0;k<n&&flag==0;k++)
			{
				if(a[k]>temp)
					flag=1;
			}
			if(flag)
			{	
				if(i!=j&&cnt2==1)
				{
					temp++;
					a[j]++;
				}
				
			}		
			else
			{
				*sum=ptemp;
				char c;
				c=65+i;
				O<<c;
				if(i!=j)
				{
					c=65+j;
					O<<c;
				}
				O<<' ';
				return 1;
			}
		}
		cnt2=0;	
				j=i;
				if(a[j]>0)
				{a[j]--;cnt2=1;temp--;}
				else
				{
				if(cnt==1)
					{a[i]++;temp++;}
				continue;
				}
				
				//cout<<j<<endl;
				
			ptemp=temp;
			temp/=2;
			bool flag=0;
			lld k=0;
			for(k=0;k<n&&flag==0;k++)
			{
				if(a[k]>temp)
					flag=1;
			}
			if(flag)
			{	
				if(cnt2==1)
				{
					temp++;
					a[j]++;
				}
				
			}		
			else
			{
				*sum=ptemp;
				char c;
				c=65+i;
				O<<c;
				if(i==j)
				{
					c=65+j;
					O<<c;
				}
				O<<' ';
				return 1;
			}
		
		if(cnt==1)
		{a[i]++;temp++;}
	}
}
void code(lld n,lld * a)
{
	lld k=1,i,sum=0;
	up(0,n,i)
	{
		sum+=*(a+i);
	}
	while(sum>0)
	check(k,&sum,n,a);
}
int main()
{

I.open("in.in",ios::in);
O.open("out.txt",ios::out);
lld t1;
lld k=1;
I>>t1;
while(k<=t1)
{
lld n;
I>>n;
lld a[n+1],i;
up(0,n,i)
I>>a[i];
O<<"Case #"<<k<<": ";
code(n,a);
O<<endl;
k++;
}
return 0;
}
