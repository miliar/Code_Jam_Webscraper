#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
#define lli long long int
lli a[1001];
int main(){
freopen("A-large.in","r",stdin);
freopen("out.txt","w",stdout);
lli t,n;
cin>>t;
for(lli k=1;k<=t;k++){
	cin>>n;
	for(lli i=0;i<n;i++)
	cin>>a[i];
	lli c1=0,c2=0;
	lli d=0;
	for(lli i=1;i<n;i++)
	{
		if(d<(a[i-1]-a[i]))
		d=a[i-1]-a[i];
	}
	
	for(lli i=1;i<n;i++)
	{
		if(d>=a[i-1])
		c2+=a[i-1];
		else
		c2+=d;
	}
	for(lli i=1;i<n;i++){
		if(a[i]<a[i-1]){
			c1+=(a[i-1]-a[i]);
		}
	}
cout<<"Case #"<<k<<": "<<c1<<" "<<c2<<endl;	
}	
}
