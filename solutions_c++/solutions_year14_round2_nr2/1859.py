#include <bits/stdc++.h>
using namespace std;
int abra(int i,int j,int k)
{
	int l;
	int a[100],b[100],c[100];
	for(l=0;l<100;l++)
	{
		c[l]=(i%2)&(j%2);
		j/=2;i/=2;
	}
	int p=1;
	int sum=0;
	for(l=0;l<100;l++)
	{
		sum+=p*c[l];p*=2;
	}
	if(sum<k)return 1;else return 0;
}
int main() {
	int a,b,k,sum,t,i,j,l;
	cin>>t;
	for(l=1;l<=t;l++)
	{
		sum=0;
		cin>>a>>b>>k;
		for(i=0;i<a;i++)
		{
			for(j=0;j<b;j++)
			{
				if(abra(i,j,k))sum++;
			}
		}
		cout<<"Case #"<<l<<": "<<sum<<endl;
	}
	// your code goes here
	return 0;
}
