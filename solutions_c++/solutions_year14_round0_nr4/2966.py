#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t,n,i,j,m,c,d,l=1;
	cin>>t;
	while(t--)
	{
		c=0;
		d=0;
		cin>>n;
		double a[n],b[n];
		for(i=0;i<n;i++)
		{
		cin>>a[i];
	    }
		for(i=0;i<n;i++)
		{
		  cin>>b[i];
        }
		sort(a,a+n);
		sort(b,b+n);
		for(j=n-1,m=n-1;j>=0;j--)
		 {
		 	if(a[j]<b[m])
		 	m--;
		 	else
		 	c++;
		 }
		 
		 for(m=0,j=n-1,i=0;m<n;m++)
		 {
		 	if(a[m]<b[i])
		 	{
		 		j--;
		 	}
		 	else
		 	{
		 		d++;
		 		i++;
		 	}
		 }
		 cout<<"Case #"<<l<<": "<<d<<" "<<c<<"\n";
		 l++;
		 
	}
	
}
