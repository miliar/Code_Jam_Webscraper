#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t,tt;
	cin>>t;
	
	for(tt=1;tt<=t;)
	{
		int n,i,j,b,a[10]={0,0,0,0,0,0,0,0,0,0};
		cin>>n;
        if(n==0)
		{
			cout<<"Case #"<<tt<<": "<<"INSOMNIA";
		}	
		
	    else
	    {
	    	for(j=1; ;)
	    	{
	    		b=n*j;
	    		for(;b>0;)
	    		{
	    			i=b%10;
	    			a[i]=a[i]+1;
	    			b=b/10;
				}
	    		if(a[0]!=0&&a[1]!=0&&a[2]!=0&&a[3]!=0&&a[4]!=0&&a[5]!=0&&a[6]!=0&&a[7]!=0&&a[8]!=0&&a[9]!=0)
	    		{
	    			cout<<"Case #"<<tt<<": "<<n*j;
					break;
				}
				j++;
			}
	    	
		}
		cout<<endl;
		tt++;
	    
	}
}