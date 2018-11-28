#include <algorithm>
#include <cstring>
#include <cmath>
#include <set>
#include <vector>
#include <cstdio>
#include <iostream>
#define S(x) scanf("%lld",&x)
#define P(x) printf("%lld",x)
#define LI long long int
using namespace std;
int main() {
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		LI n,a[26],total=0;
		char ch;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>a[i];
			total+=a[i];
		}
		//cout<<total<<endl;
		cout<<"Case #"<<k<<": ";
		while(total>0)
		{
			
			LI largest,slargest;
			if(n==2)
			{
				
				largest=0;
				slargest=1;
				if(a[largest]<a[slargest])
				{
					 largest=1;
					 slargest=0;
				 }
				 if(a[largest]>a[slargest]+1)
				 {
					 ch=65+largest;
					 a[largest]-=2;
					 total-=2;
					 cout<<ch<<ch<<" ";
				 }
				 else if(a[largest]>a[slargest])
				 {
					 ch=65+largest;
					 a[largest]-=1;
					 total-=1;
					 cout<<ch<<" ";
				 }
				 else
				 {
					    ch=65+largest;
					    a[largest]-=1;
					    total-=1;
					    cout<<ch;
					    
						ch=65+slargest;
					    a[slargest]-=1;
					    total-=1;
					    cout<<ch<<" ";
				 }
				 //cout<<total<<" "<<largest<<"  "<<slargest<<endl;
				 //cout<<a[largest]<<"  "<<a[slargest]<<endl;
			}
			else
			{
				largest=0;
				slargest=1;
				if(a[largest]<a[slargest])
				{
					 largest=1;
					 slargest=0;
				}
				for(int i=2;i<n;i++)
				{
					if(a[i]>a[largest])
					{
						slargest=largest;
						largest=i;
					}
					else if(a[i]>a[slargest])
					{
						slargest=i;
					}
				}
				if(a[largest]>a[slargest]+1)
				{
					ch=65+largest;
					 a[largest]-=2;
					 total-=2;
					 cout<<ch<<ch<<" ";
				}
				else if(a[largest]>a[slargest])
				 {
					 ch=65+largest;
					 a[largest]-=1;
					 total-=1;
					 cout<<ch<<" ";
				 }
				 else if(a[largest]==a[slargest])
				 {
					 if(total>a[largest]+a[slargest])
					 {
						ch=65+largest;
					    a[largest]-=1;
					    total-=1;
					    cout<<ch<<" ";
					 }
					 else if(total==a[largest]+a[slargest])
					 {
						 
						ch=65+largest;
					    a[largest]-=1;
					    total-=1;
					    cout<<ch;
					    
						ch=65+slargest;
					    a[slargest]-=1;
					    total-=1;
					    cout<<ch<<" ";
					 }
				 }
			}
		}
		cout<<endl;
	}
	return 0;
}
