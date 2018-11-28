#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int main()
{   
	freopen("B-small-attempt6.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int t,tt;
	cin>>t;
	for(tt=1;tt<=t;)
	{
		int n,i,j,s=0;
		char a[100];
		scanf("%99s",&a);
		n=strlen(a);
		for(i=0;i<n;)
		{
			j=i;
			for(;i<n;)
			{
				if(a[i]==a[j])
				{
				++i;
				continue;
			    }
				else 
				{
				j=i;
				++s;
				break;
			    }
			}
			
			
			
		}
		if(a[n-1]=='-')
		cout<<"Case #"<<tt<<": "<<s+1;
		else
		cout<<"Case #"<<tt<<": "<<s;	
		
	    cout<<endl;
	    tt++;
	    
	}
	return 0;
	
}
