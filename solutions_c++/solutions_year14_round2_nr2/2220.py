#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iomanip>
#include<cmath>
#include<vector>
#include<set>
#include<map>
using namespace std;
typedef long long int ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
#define rep(i,n)   for(int i=0;i<n;i++)
#define rrep(i,n)  for(int i=n-1;i>=0;i--)
int main()
{
	int t,tt,a,b,k;
	cin>>tt;
	for(int t=1;t<=tt;t++)
	{
		int cnt = 0;
		cin>>a>>b>>k;
		for(int i=0;i<a;i++){
			for(int j=0;j<b;j++){
				if((i&j) < k)
					cnt++;
			}
		}
		cout<<"Case #"<<t<<": "<<cnt<<endl;
	}
	return 0;
}
