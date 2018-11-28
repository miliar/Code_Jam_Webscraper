#include<bits/stdc++.h>
using namespace std;
int n=16,j=50;
int prime(long long x)
{
	int p=(int)sqrt(x);
	int i;
	for(i=2;i<=p;i++)if(x%i==0)return i;
	return 0;
}
bool a[16];
long long convert(int base)
{
	long long answer=0,temp=1;
	int i;
	for(i=15;i>=0;i--)
	{
		if(a[i]==1)answer+=temp;
		temp*=base;
	}
	return answer;
}
void dojob()
{
	int p=16384,i,k,l,m,n;
	for(i=0;i<p;i++)
	{
		k=i;
		for(l=1;l<=14;l++)
		{
			a[l]=k%2;
			k/=2;
		}
		for(k=2;k<=10;k++)if(prime(convert(k))==0)break;
		if(k==11)
		{
			for(m=0;m<=15;m++)cout<<(int)a[m];
			cout<<" ";
			for(m=2;m<=10;m++)cout<<prime(convert(m))<<" ";
			cout<<endl;
			j--;
		}
		if(j<=0)break;
	}
}
int main()
{
	a[0]=1;a[15]=1;
	int t;cin>>t;
	cin>>n>>j;
	cout<<"Case #1: \n";
	dojob();
}
