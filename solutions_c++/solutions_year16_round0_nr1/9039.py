#include<bits/stdc++.h>
using namespace std;
int match(int a[],int r);
int main()
{
	int tc,i,j=0,r,k;long int n,ans,m;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>tc;
	while(tc--)
	{
		cin>>ans;
		i=0;n=0;r=0;k=1;
		int a[10]={0};
		
		if(ans==0)
		cout<<"case #"<<++j<<": "<<"INSOMNIA"<<endl;
		else
		{ n=ans;
	    	while(1)
			{   
			    while(n>0)
				{
					r=n%10;
					n=n/10;
					if(match(a,r)==1)
					{
					a[r]=1;
					i++;
				}
					if(i==10)
					break;
				}
				if(i==10)
				break;
				n=m=ans*(++k);
			}
			cout<<"case #"<<++j<<": "<<m<<endl;
			
			}
	}
	return 0;
}
int match(int a[],int r)
{
	int f=0;
	if(a[r]==0)
	return 1;
	else
	return 0;
}
