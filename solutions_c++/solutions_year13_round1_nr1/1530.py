#include<stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#include<string.h>
using namespace std;


int i,it,T,n,r,t,j,k,f,p[10000],sum[10000];

int main()
{
	 freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	/*I3 7 11 15
	for(i=1;i<=2000;i++)
		p[i]=i*i;
	for(j=1;j<=1000;j++)
		sum[j]=p[j*2]-p[j*2-1];
*/
	cin>>T;
	for(it=1;it<=T;it++)
	{
	//
	cin>>r>>t;
	k=0;
	f=(r+1)*(r+1)-r*r;
	while(t>=f)
	{
		//cout<<f<<endl;
		k++;
		t-=f;
		r+=2;
		f=(r+1)*(r+1)-r*r;
	}

	cout<<"Case #"<<it<<": "<<k<<endl;
	//for(j=1;j<=14;j++)
	//	cout<<sum[j]<<endl;
	}	
	return 0;
}