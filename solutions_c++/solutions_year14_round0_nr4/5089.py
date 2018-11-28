#include <iostream>
#include <algorithm>
using namespace std;
#define M 10
int main() {
	double a[M],b[M];
	int i,t,n,s,j,z,g,l,h;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		cin>>n;
		s=0;
		g=0;
		l=0;
		for(i=0;i<n;i++)
			cin>>a[i];
		for(i=0;i<n;i++)
			cin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		
		
			
			i=0;
			j=0;
			while(i<n && j<n)
			{
				if(a[i]<b[j])
				{	
					l++;
					i++;
					j++;
				}
				else
				{	
					
					g++;
					j++;
				}
			}
			i=n-1;
			j=n-1;
			while(i>=0 && j>=0)
			{
				if(a[i]>b[j])
				{
					i--;
					j--;
					s++;
				}
				else
				{
					j--;
						
				}
			}
			
		
		
		cout<<"Case #"<<z<<": "<<s<<' '<<g<<endl;
	}
	return 0;
}