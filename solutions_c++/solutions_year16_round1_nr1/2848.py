#include<bits/stdc++.h>

using namespace std ;
#define ll long long 

char ch[5000],arr[10000];
int main()
{
	freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);	 
	 ll t,n;
	 cin>>t;
	  for(int z=1;z<=t;z++)
	 {  cin>>ch;
	     n=strlen(ch);
	     arr[n]=ch[0];
	     int start=n-1,end=n+1;
	     
	     for(int i=1;i<n;i++)
	     {
	     	if(ch[i]<arr[start+1])
	     	{
	     		arr[end++]=ch[i];
			 }
			 else
			 arr[start--]=ch[i];
		 }
		 
	 	cout<<"Case #"<<z<<": ";
	 	for(int i=start+1;i<end;i++)
	 	{
	 		cout<<arr[i];
		 }
		 cout<<endl;
	 	
	  } 
}
	
	

