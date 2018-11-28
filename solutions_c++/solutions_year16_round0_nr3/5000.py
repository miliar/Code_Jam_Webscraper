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

LI inc(LI a[],LI n)
{
	LI set=0;
	for(int i=n-1;i>1;i--)
	{
		if(a[i]==0 && set==0)
		{
			 a[i]=1;
			 return 0;
		 }
		else if(a[i]==1)
		{
			 if(set==0) set=i;
		 }
		else if(a[i]==0 && set>0)
		{
			for(int j=i+1;j<=set;j++) a[j]=0;
			a[i]=1;
			return 0;
		}
		
	}
	return -1;
}
LI find_prime(LI x)
{
	int temp=sqrt(x);
	for(int i=2;i<temp;i++)
	{
		if(x%i==0) return i;
	}
	return 0;
}

int main() {
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		LI n,j,a[100],jc[51][11],count=0,b[51][20];// jc keeps divisors and b keep jamcoin a
		S(n);
		S(j);
		a[1]=1;
		a[n]=1;
		for(int i=2;i<n;i++) a[i]=0;
		while(count<=j)
		{
			
			//for(int i=1;i<=n;i++)cout<<a[i];
			//cout<<endl;
			//count++;
			LI temp[11],c=1;//c tells wheather to check or not
			for(int i=2;i<=10;i++)
			{
				LI mul=1,num;
				num=0;
				for(int it=n;it>=1;it--)
				{
					num+=mul*a[it];
					mul*=i;
				}
				temp[i]=find_prime(num);
				if(temp[i]==0)
				{
					c=0; 
					break;
				}
			}
			if(c==1)
			{
				for(int i=2;i<=10;i++)
				{
					jc[count][i]=temp[i];
				}
				for(int i=1;i<=n;i++) b[count][i]=a[i];
				count++;
			}
			inc(a,n);
		}
		cout<<"Case #"<<k<<":"<<endl;
		for(int i=1;i<=j;i++)
		{
			for(int it=1;it<=n;it++) cout<<b[i][it];
			cout<<" ";
			for(int it=2;it<=10;it++) cout<<jc[i][it]<<" ";
			cout<<endl;
		}
	}
	return 0;
}
