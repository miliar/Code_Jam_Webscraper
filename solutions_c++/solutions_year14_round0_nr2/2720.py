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
	freopen("Bsmall.txt","r",stdin);
	freopen("BsmallOut.txt","w",stdout);	
	int test;
	
	cin>>test;
	int count = 1;
	while(test--)
	{
		
		
		double c,f,x;
		scanf("%lf %lf %lf",&c,&f,&x);
		
		double min[10000]={0};
		
		//int total = x/c;
		
		//cout<<total;
		double cookie = 2;
		double sum = 0;
		int i=0;
		double temp=0;
		while(temp!=x)
		{
			double temp2 = x/cookie;
			
			double t1 = c/cookie;
			
			double t2 = x/(cookie+f);
			if((t1+t2)<temp2)
            {
            	cookie+=f;
              	sum+=t1;
              	//index++;
           	}
           	else
           	{
           		
           	   	temp=x;
               	sum+=temp2;
           	}
			
		}

		printf("Case #%d: %.7lf\n",count,sum);
		
		
		count++;
	}
	return 0;
}
