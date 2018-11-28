#include <iostream>
#include <sstream>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <string.h>
#include <cmath>
#include <utility>
#include <algorithm>
#include <cassert>
#include <stdio.h>
#include <iomanip>
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
#define fastio std::ios_base::sync_with_stdio(false)

int main()
{
	int T,ctr;
	ll N,temp;
	set<int> arr;
	ctr=1;
	cin>>T;
	while(T--)
	{
		cin>>N;
		if(N==0)
		{
			cout<<"Case #"<<ctr<<": INSOMNIA"<<endl;
		}
		else
		{
			arr.clear();
			for(temp=N;;temp+=N)
			{
				ll num=temp;
				while(num)
				{
					arr.insert(num%10);
					num/=10;
				}

				if(arr.size()==10)
					break;
			}

			cout<<"Case #"<<ctr<<": "<<temp<<endl;
		}

		ctr++;
	}
}