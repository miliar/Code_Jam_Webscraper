
/* Written by 
   D.Anil SaiKrishna 
   */

#include<bits/stdc++.h>
using namespace std;

char arr[1010];

int main()
{
	ios_base::sync_with_stdio(0);
	int t,m,s,i,b,ct=1,n,idx,min;
	cin>>t;
	while(t--){

	cin>>s;
	int count=0,ans=0;
	for(i=0;i<=s;i++)	
	{
	cin>>arr[i];
	n=arr[i]-48;
	if(i>count){
	ans=ans+(i-count);	
	count=i;		
	}
	count+=n;	
}
cout<<"Case #"<<ct<<": "<<ans<<endl;
ct++;
	}
	return 0;
}