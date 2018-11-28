#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
using namespace std;
#define MAX 10000001
vector <long long int> fspalin;
bool check_palin(long long int n)
{
	long long int t=0;
	long long int a=n;
	while(a!=0)
	{
		t=t+a%10;
		a/=10;
		if(a>0)t*=10;
	}
	if(n==t)return true;
	else return false;
}
void preprocess()
{
	for(long long int i=1;i<MAX;i++)
	{
		if(check_palin(i))
		{
			if(check_palin(i*i))fspalin.push_back(i*i);
		}
	}
}
long long int binSearch(long long int n)
{
	long long int m,l=0,u=fspalin.size()-1;
	while(l<=u)
	{
		if(l==u)
		{
			if(fspalin[l]>n)return l;
			else return l+1;
		}
		long long int m=(l+u)/2;
		if(fspalin[m]==n)return m+1;
		else if(fspalin[m]>n)u=m-1;
		else l=m+1;
	}
}
int main()
{
	long long int a,b;
	int t;
	preprocess();
	scanf("%d",&t);
/*	for(int i=100;i<1001;i++)
		if(num[i]!=num[i-1])cout<<i<<" "<<num[i]<<endl;*/
	for(int k=1;k<=t;k++)
	{
		scanf("%lld%lld",&a,&b);
		printf("Case #%d: %lld\n",k,binSearch(b)-binSearch(a-1));
	}
	return 0;
}
