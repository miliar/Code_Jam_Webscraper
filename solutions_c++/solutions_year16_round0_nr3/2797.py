#include <iostream>
#include<cstring>
using namespace std;

#define m 65535
#define l 32769
int mp[m+1]={0};
string convert(int k,int base)
{
	int t=k;
	string s;
	while(t)
	{
		char c='0'+t%base;
		t/=base;
		s=c+s;
	}
	return s;
}

long long int c2(string s,int base)
{
	long long int i=0,n=0;;
	for(;i<s.length();i++)
	{	int a=s[i]-'0';
		n=n*base+a;
	}
	return n;
}


long long int isprime(long long int n)
{
	long long int j=2;
	
	for(;j*j<=n;j++)
	{
		if(n%j==0)
		{
			return j;
		}
	}
	return -1;
}


int main() {
	// your code goes here
	
	int i=2,j,n,jt,t;
	cin>>t>>n>>jt;
	
	for(i=2;i*i<=m;i++)//preparing the sieve
	{
		if(!mp[i])
		{
			for(j=i*i;j<=m;j+=i)
			{
				if(!mp[j])
				{
					mp[j]=i;
				}
			}
			
		}
	}
	
	string s;
	int x=l;
	int count=0;
	cout<<"Case #1:";
	for(;x<=m;x+=2)
	{
		if(mp[x])
		{
			string s=convert(x,2);
			//cout<<"s="<<s<<"\n";
			int flag=0;
			long long int art[11]={0};
			memset(art,0,11);
			for(i=2;i<=10;i++)
			{
				long long int d=c2(s,i);
				//cout<<"d= "<<d<<"\n";
				if(isprime(d)==-1)
				{
					flag=1;
				//	cout<<"a";
					break;
				}
				else
				{
				 art[i]=isprime(d);	
				}
			}
			if(!flag)
			{
				cout<<"\n"<<s<<" ";
				for(i=2;i<=10;i++)
				{
					cout<<art[i]<<" ";
				}
				count++;
				if(count==jt)
			    	{
			    		break;
			    	}
				//cout<<jt<<" ";
			}
		}
	}
	return 0;
}