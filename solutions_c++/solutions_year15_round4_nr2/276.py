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
#include <iomanip>  
using namespace std;

//typedefs
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int, int> pii;
typedef pair<long long, long long> pll;
typedef pair<ld,ld> pld;

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
	//ld r[111], c[111];
	pld cr[111];
	ll test;
	sl(test);
	repii(tt,1,test)
	{
		printf("Case #%lld: ", tt);
		ll nn; 
		ld v, x;
		cin>>nn>>v>>x;
		ld mass = 0.0;
		ld totr = 0.0;
		bool left = false;
		bool right = false;
		ld reserve = 0.0;
		ll ptr = 0;
		repi(i,0,nn)
		{
			//cin>>r[i]>>c[i];
			ld r, c;
			cin>>r>>c;
			//cin>>cr[i].ss>>cr[i].ff;
			if(x != c)
			{
				cr[ptr].ss = r;
				cr[ptr].ff = c;
				mass += cr[ptr].ss*cr[ptr].ff;
				totr += cr[ptr].ss;
				ptr++;
			}
			else
			{
				reserve += r;
			}
			
			if(c > x) left = true;
			if(c < x) right = true;
		}
		if(!( (left and right) || (reserve != 0.0)))
		{
			//impossible
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if((!left) || (!right))
		{
			cout<<v/reserve<<endl;
			continue;
		}

		sort(cr,cr+ptr);
		ld anss = 0;
		ld av = mass/totr;
		if(av==x)
		{
			anss = v/(totr+reserve);
		}
		else if(av<x) // its gonna be so cold !!!
		{
			//cout<<"thanda "<<endl;
			ll i = 0;
			while(i<ptr)
			{
				//cout<<"i = "<<i<<endl;
				mass -= cr[i].ss*cr[i].ff;
				totr -= cr[i].ss;
				av = mass/totr;
				if(av>=x)
					break;
				i++;
			}
			if(true)
			{
				if(cr[i].ff-x == 0.0)
				{
					anss = v/(totr+reserve);
				}
				else
				{
					ld mera = (mass - x*totr)/(x-cr[i].ff);
					mass += mera*cr[i].ff;
					totr += mera;
					av = mass/totr;
					anss = v/(totr+reserve);
				}
			}
			else
			{
				//impossible
				anss = -1;
			}
		}
		else //its gonna be so hot
		{
			//cout<<"garam"<<endl;
			ll i = ptr-1;
			while(i>=0)
			{
				//cout<<"i = "<<i<<endl;
				mass -= cr[i].ss*cr[i].ff;
				totr -= cr[i].ss;
				av = mass/totr;
				//cout<<"mass = "<<mass<<endl;
				//cout<<"totr = "<<totr<<endl;
				//cout<<"av = "<<av<<endl;
				if(av<=x)
					break;
				i--;
			}
			if(true)
			{
				if(cr[i].ff-x == 0.0)
				{
					anss = v/(totr+reserve);
				}
				else
				{
					ld mera = (mass - x*totr)/(x-cr[i].ff);
					mass += mera*cr[i].ff;
					totr += mera;
					av = mass/totr;
					anss = v/(totr+reserve);
				}
			}
			else
			{
				//impossible
				anss = -1;
			}
		}
		if(anss > 0)
		{
			cout << std::setprecision(17) <<anss<<endl;
		}
		else
		{
			cout<<"IMPOSSIBLE2"<<endl;
		}
	}
	return 0;
}