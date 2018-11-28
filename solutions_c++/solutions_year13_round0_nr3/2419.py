
/*
Author Name::Himanshu Tomar
Lang::C++
*/

// header files

#include<iostream>
#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cassert>
#include<utility>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
#include<iomanip>
#include<map>
#include<set>
#include<ctime>
#include<cstring>
#include<cmath>
#include <stdlib.h>
#include <unistd.h>
#include <stdint.h>

// definitions

#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define ppb() pop_back()
#define ll long long int
#define s(a) scanf("%d",&a)
#define clr(x) memset(x,0,sizeof(x))
#define bs(a,b,c) binary_search(a,b,c)
#define ub(a,b,c) upper_bound(a,b,c)
#define lb(a,b,c) lower_bound(a,b,c)
#define mod 1000000007
using namespace std;

ll rs(ll x)
{
ll z=0;
	while(x>0)
	{
	z=z*10+x%10;
	x/=10;
	}
return z;
}

int main()
{
     freopen("C:\\Users\\JI\\Desktop\\input.txt","r",stdin);
     freopen("C:\\Users\\JI\\Desktop\\output.txt","w",stdout);
      int tc,in=1;
      vector<ll> v;
      	vector<ll>::iterator it;
			for(ll i=1;i<=10000000;i++)
			{
				if(i==rs(i) and i*i==rs(i*i))
					v.pb(i*i);
			}
      s(tc);
      while(tc--)
      {
      	ll cc=0;
      	
             ll a,b;
             scanf("%lld%lld",&a,&b);
             for(it=v.begin();it!=v.end();it++)
			 {
			 	if((*it)<=b and (*it)>=a)
					cc++;
			 }
                 printf("Case #%d: %lld\n",in,cc);
                 in++;
      }
      return 0;
}