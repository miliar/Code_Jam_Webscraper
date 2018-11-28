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
  freopen ("A-small-attempt1 (1).in", "r", stdin);
  freopen ("Asmallout.in", "w", stdout);
  int t,cs=1,w,c,r,ans;
  cin>>t;
  while(t--)
  {
  		cin>>r>>c>>w;
  		
  		if(w==1)
  		ans=c;
  		else
  		{
  		  ans=w;
  		  c-=w;
  		  if(c%w==0)
  		  ans+=c/w;
  		  else
  		  ans+=((c/w)+1);
  		}
  		cout<<"Case"<<" #"<<cs++<<": "<<ans<<"\n";
  } 
  return 0;
}

