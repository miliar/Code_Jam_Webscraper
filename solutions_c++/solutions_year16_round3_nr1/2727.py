#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int t,i,j,k,l,m,n,o,p,h,h1;
	cin>>t;
	o=1;
	while(t--)
	{
		h=h1=0;
		k=l=0;
		cout<<"Case #"<<o++<<": ";
		cin>>n;
		long long int a[n];
		for(i=0;i<n;i++)
		{
			cin>>a[i];
			if(a[i]>h1)
			{
				h1=a[i];
				l=i;  
			}
			
			if(a[i]>h)
			{
				h1=h;
				h=a[i];
				l=k;
				k=i;
				
			}
			
			
		}
		
	//	cout<<l<<" "<<k;  //secong high hishest
		
		j=a[k]-a[l];
		
		while(j>=2)
		{
			char c='A'+k;
			cout<<c<<c<<" ";
			j-=2;
			a[k]-=2;
		}
		
		if(j==1)
		{
			char c='A'+k;
			cout<<c<<" ";
			j--;
			a[k]--;
		}
		
		
		for(i=0;i<n;i++)
		{
			char c;
			if(i!=k && i!=l){
			while(a[i]>=2)
			{
				c='A'+i;
				cout<<c<<c<<" ";
				a[i]-=2;
			}
			if(a[i]==1){
			char c='A'+i;
			cout<<c<<" ";
			a[i]=0;
				}
			}
		}
		
		//cout<<a[k]<<a[l]<<" ";
		
		for(i=0;i<a[k];i++)
		{
			char q='A'+l;
			char w='A'+k;
			cout<<q<<w<<" ";
			//a[k]--;
		}
		
		cout<<"\n";
		
	}
}
