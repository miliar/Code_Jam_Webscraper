#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output1.txt", "w", stdout);
	long long int t,smax,temp,n,j,i,s;
	char a[10000];
	cin>>t;
	for(n=0;n<t;n++)
	{
		smax=0;
		temp=0;
		cin>>s;
	    cin>>a;
	    for(i=1;i<=s;i++)
	    {
	    	temp=temp+a[i-1]-48;
	      	if(i>temp)
	      	{
	            smax=smax+i-temp;
	            j=i-temp;
				temp=temp+j;	
	      	}
	      	
	    }
	    cout<<"Case #"<<n+1<<":"<<" "<<smax<<"\n";
	}
	return 0;
}
