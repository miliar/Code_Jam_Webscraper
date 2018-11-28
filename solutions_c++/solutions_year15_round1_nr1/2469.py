#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
#define mod 1000000007
using namespace std;
int main()
{
  std:ios_base::sync_with_stdio(false);
  freopen ("A-large.in", "r", stdin);
  freopen ("Alargeout.in", "w", stdout);
  int curr,tmp,t,n,i,ans1,ans2,cs=1,diff,j;
  
  
  cin>>t;
  while(t--)
  { ans1=0; ans2=0;
  	cin>>n;
    int a[n+1];
  	
  	for(i=0;i<n;i++)	cin>>a[i];
  	
  	for(i=0;i<n-1;i++)
  	{
  		diff=a[i+1]-a[i];
  		
  		if(diff<0)
  		ans1+=(-diff);
  	}
  	
  	diff=-1;
  	for(i=0;i<n-1;i++)
  	{
  		diff=max(diff,a[i]-a[i+1]);
  	}
  	//cout<<diff<<"\]";
  		for(i=0;i<n-1;i++)
  		{
  			//curr=a[i+1]-a[i];
  			
  			ans2+=min(diff,a[i]);
  			
  			
  		}
  		
  	
  	
  	cout<<"Case"<<" #"<<cs++<<": "<<ans1<<" "<<ans2<<"\n";
  	
  }
  
  return 0;
}

