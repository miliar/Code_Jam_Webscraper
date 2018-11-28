#include<iostream>
#include<stdio.h>
#include<string>
using namespace std;
int main()
{
	int t,x,i,p,f,k;
	cin>>t;
	for(x=1;x<=t;x++)
	{
		char a[5000];
		scanf("%s",&a);
		char p;
		p=a[0];
		char c[5000];
		k=2000;
		f=2001;
		c[k--]=p;
		
		for(i=1;a[i]!='\0';i++)
	    {
	    	if(a[i]>=p)
	    	{
	    		p=a[i];
	    			c[k--]=p;
			}
		    else
		    {
		    	c[f++]=a[i];
			}
		}
//		char ans[5000];
        cout<<"Case #"<<x<<": ";
		for(i=k+1;i<f;i++)
		{
			cout<<c[i];
		}
		cout<<endl;
	}
}