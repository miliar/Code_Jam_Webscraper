#include<stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int a,b,c[100],l,ic,j,it,T,i,m,s,n,k,e,q;
int p[100000];
//char s[100][100];
bool wx,prt;

bool w(int x)
{
//	cout<<x<<endl<<" ***    ";
	prt=true;
	l=0;
	while(x>0)
	{
		c[l]=x%10;
//		cout<<c[l]<<" ";
		l++;
		x/=10;
	}

	//if(l%2=0){
	for(ic=0;ic<l;ic++)
	{
		if(c[ic]!=c[l-ic-1])
		{	
			prt=false;
			break;
		}
	}
	
	return prt;
}
int main()
{
	 freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

//	while(cin>>T)
//		cout<<w(T)<<endl;
	for(i=1;i<40;i++)
	{
		if(w(i) && w(i*i))
			p[i*i]=1;
	}
	cin>>T;
	for(it=0;it<T;it++)
	{
		cin>>a>>b;
//		cout<<"***   "<<endl;
		int sum=0;
		for(i=a;i<=b;i++)
			if(p[i]==1)
			{
				sum++;
//		cout<<i<<"  ";
		}
		cout<<"Case #"<<it+1<<": "<<sum<<endl;

	}
	return 0;
}