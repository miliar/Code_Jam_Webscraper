//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>

using namespace std;

//typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;

//defines-general
#define to(a) __typeof(a)
#define all(vec)  vec.begin(),vec.end()
#define fill(a,val)  memset(a,val,sizeof(a))

//defines-iteration
#define repi(i,a,b) for(__typeof(b) i = a;i<b;i++)
#define repii(i,a,b) for(__typeof(b) i = a;i<=b;i++)
#define repr(i,b,a) for(__typeof(b) i = b;i>a;i--)
#define repri(i,b,a) for(__typeof(b) i = b;i>=a;i--)
#define tr(vec,it)  for(__typeof(vec.begin())  it = vec.begin();it!=vec.end();++it)



//defines-pair
#define ff first
#define ss second
#define pb push_back
#define mp make_pair

// my own
#define sl(a) scanf("%lld",&a)
#define sll(a,b) scanf("%lld%lld",&a,&b)
#define slll(a,b,c) scanf("%lld%lld%lld",&a,&b,&c)
#define sllll(a,b,c,d) scanf("%lld%lld%lld%lld",&a,&b,&c,&d)

int main()
{
	ll test;
	sl(test);
	repii(tt,1,test)
	{
		printf("Case #%lld: ", tt);
		ll n,x;
		sll(n,x);
		//cout<<"taken x n"
		vector<ll> arr(n);
		repi(i,0,n) sl(arr[i]);
		sort(arr.begin(), arr.end());
		//repi(i,0,n) cout<<arr[i]<<" ,";
		//cout<<endl;
		ll disks = 0;
		while(arr.size()>1)
		{
			//cout<<"inwhile "<<arr.size()<<endl;
			ll big = *(arr.rbegin());
			
			ll rem = x - big;
			//cout<<"big = "<<big<<" rem = "<<rem<<endl;
			vector<ll> :: iterator it = lower_bound(arr.begin(), arr.end(),rem);
			if(it == arr.begin()&&(*it != rem))
			{
				//cout<<"no match"<<endl;
				arr.pop_back();
			}
			else if(it == arr.end())
			{
				//cout<<"all match"<<endl;
				arr.pop_back();
				arr.pop_back();
			}
			else
			{
				if(*it != rem)
				it--;
				//cout<<"match "<<*it<<endl;
				arr.erase(it);
				arr.pop_back();
			}
			disks++;
		}
		if(arr.size()) 
		{
			disks++;
		}
		printf("%lld\n",disks );
	}
	return 0;
}