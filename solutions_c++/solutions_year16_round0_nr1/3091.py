#include <stdio.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <stdlib.h>
#include <math.h>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>
using namespace std;
#define ll long long 
#define _ ios::sync_with_stdio(false);
#define mem(x,a) memset(x,(a),(int)(sizeof(x)))
#define pii pair<int,int>
#define fr(i,a,n) for(int i=(a);i<=(n);i++)
#define frd(i,a,n) for(int i=(a);i>=(n);i--)
#define nl printf("\n")
#define pb push_back
#define mp make_pair 
#define F first 
#define S second
#define V vector
ll mod=1e9+7;
int main() {_
	int t;cin>>t;
	fr(k,1,t)
	{
		ll n;cin>>n;
		if(n==0LL)
		{
			cout<<"Case #"<<k<<": INSOMNIA\n";
			continue;
		}
		int cnt[20]={0},rem=10;
		ll ans=0;
		for(ll i=1;;i++)
		{
			ll num=n*i;
			//cout<<num<<endl;
			if(rem==0)break;
			while(num)
			{
				cnt[num%10LL]++;
				if(cnt[num%10LL] == 1)rem--;
				if(rem==0){
					ans=n*i;
					break;
				}
				num/=10LL;
			}
		}
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}
