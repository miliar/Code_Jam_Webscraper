#include <bits/stdc++.h>
using namespace std;
#define ll long long 
bool arr[20];
bool check ( ll  x)
{
	while(x>0)
	{
		ll  r=x%10;
		arr[r]=true;
		x=x/10;
	}
	for(ll  i=0;i<10;i++)//cout<<arr[i]<<" ";cout<<"\n";
	if(!arr[i])return true;
	return false;
}
int  main()
{
	ll  t;
	cin>>t;
	ll  p=1;
	while(t--)
	{
		ll  n=p;
	    cin>>n;
		ll  i=1;
		if(n==0){cout<<"Case #"<<p<<":"<<"INSOMNIA\n";p++;continue;}
	    while(check(i*n))
	    {
	    	i++;
		}
	
		memset(arr,false,sizeof(arr));
		cout<<"Case #"<<p<<":"<<i<<"\n";
		p++;
	    
    }
}
