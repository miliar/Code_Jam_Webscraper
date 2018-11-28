#include <iostream>
#include <cstdio>
#include <utility>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <bits/stdc++.h>
using namespace std;


#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define ll long long 
int main()
{
   freopen("in1.txt","r",stdin);
   freopen("out1.txt","w",stdout);
   int T;
   cin>>T;
   for(int test=1;test<=T;test++)
   {
	  int n,x;
	  cin>>n>>x;
	  int a[n];
	  
	  for(int i=0;i<n;i++) cin>>a[i]; 
	  
	  sort(a,a+n);
	  int f =0;
	  int r=n-1;
	  int h[2000000]={0};
	  int c=0;
	  while(f<r)
	  {
		  while(r>=0 && (a[f]+a[r])>x)
		  {
			  r--;
		  }
		  if(r<0) break;
		  if(a[f]+a[r]<=x) 
		  {
			  h[f]=1;
			  h[r]=1;
			  r--;
			  f++;
			  c++;
		  } 
	  }
	  for(int i=0;i<n;i++) if(!h[i]) c++;
	  printf("Case #%d: ",test);
	  cout<<c<<endl;
   }   
   return 0;
}
