//header files
 
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<cstring>
using namespace std;
 
//end of header files
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define FOR(i,n)                for(int i=0;i<n;i++)  
#define FOR2(i,n)                for(int i=1;i<=n;i++)  
#define inf 1000000000
#define   M 1000000007
 
#define maxn 1000000
#define maxt 100000
typedef long long int LL;
typedef long long int lld;
typedef long int ld;
 
int main()
{
	freopen("Dsmall.txt","r",stdin);
	freopen("DsmallOut.txt","w",stdout);	
	int test;
	
	cin>>test;
	int count = 1;
	while(test--)
	{
		int n;
		cin>>n;
		bool check[n+1];
		bool check2[n+1];
		double a[n+1],b[n+1];
		
		for(int i=0;i<n;i++)	
		{
			cin>>a[i];
			check[i] = false;
			check2[i] = false;
		}
		
		for(int i=0;i<n;i++)	
		{
			cin>>b[i];
		}
		
		
		sort(a,a+n);
		
		sort(b,b+n);
		reverse(a,a+n);
		reverse(b,b+n);
			/*
		for(int i=0;i<n;i++)	
		{
			cout<<a[i]<<" ";
			
		}
		cout<<endl;
		
		for(int i=0;i<n;i++)	
		{
			cout<<b[i]<<" ";
		}
		cout<<endl;
		*/
		
		int deceitWar = 0;
		
		for(int i=0;i<n;i++) 
		{
			for(int j=0;j<n;j++)
			{
				if(a[i]>b[j]&&!check2[j])
				{
					deceitWar++;
					check2[j] = true;
					break;
				}
			}
		}
		
		
		int War = 0;
		
		for(int i=0;i<n;i++)
		{
			double temp = b[i];
			
			for(int j=0;j<n;j++)
			{
				if(temp>a[j]&&!check[j])
				{
					War++;
					check[j] = true;
					break;
				}
				
			}
		}
		
		
		cout<<"Case #"<<count<<": "<<deceitWar<<" "<<n-War<<endl;
		
		
		
		
		count++;
	}
	return 0;
}
