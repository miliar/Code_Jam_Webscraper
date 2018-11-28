#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<sstream>
#include<set>
#include<climits>
#define gc getchar
#define f first
#define s second
#define TEST ll T = scan(); for(int t=1; t<=T; t++)
#define D(x) ll x = scan()
using namespace std;
typedef long long ll;
#define rep(i, n) for(ll i=0; i<n; i++)
ll scan() 
{
  char c = gc();
  while(c<'0' || c>'9') c = gc();
  ll ret = 0;
  while(c>='0' && c<='9') {
    ret = 10 * ret + c - 48;
    c = gc();
  }
  return ret;
}
int main()
{
	TEST
	{
		int arr[100111], n;
		int i,diff=0, x=0, y=0;
		cin>>n;
		for(i=1;i<=n;i++)
			cin>>arr[i];
		x=0;y=0;
		for(i=1;i<n;i++)
		{
			if(arr[i]>arr[i+1])
				x+=arr[i]-arr[i+1];
		}
		for(i=2;i<=n;i++)
		{
			if(arr[i-1]>arr[i])
				diff=max(diff,arr[i-1]-arr[i]);
		}
		for(i=1;i<n;i++)
		{
			y+=min(diff,arr[i]);
		}
		cout<<"Case #"<<t<<": "<<x<<" "<<y<<endl;;
	}
	return 0;
}
