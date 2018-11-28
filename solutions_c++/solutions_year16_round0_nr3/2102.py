#include <string>
#include <vector>
#include <map>
#include <list>
#include <iterator>
#include <set>
#include <queue>
#include <iostream>
#include <sstream>
#include <stack>
#include <deque>
#include <cmath>
#include <memory.h>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <algorithm>
#include <iomanip>
#include <utility> 

using namespace std;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FILL(A,value) memset(A,value,sizeof(A))

#define all(V) V.begin(), V.end()
#define sz(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define Pi 3.14159265358979

#define pp(a) cout<<a[i].first<<" "<<a[i].second<<"\n";

typedef long long ll;
typedef unsigned long long llu;
typedef vector <ll> vi;
typedef long double ld;
typedef pair <ll, ll> pii;

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

vi a;

int isprime(llu x)
{
	if(x==2) return 1;

	FOR(i,2,sqrt(x)+1)
		if(x%i==0){a.pb(i);return 0;}

	return 1;
}

llu conv(llu x,llu b)
{
	llu p=1,s=0;

	while(x>0)
	{
		s+=(x%10==1)?p:0;
		x/=10;
		p*=b;
	}

	return s;
}

int test(llu x)
{	
	llu p;

	FOR(i,2,11)
	{	
		p=conv(x,i);
		if(isprime(p)) return 0;
	}

	return 1;
}

void genbinary(int l, int j)
{
    queue<string> q;llu p,x;int f;

    q.push("1");

    llu n = (2<<(l+1));
 
    while (n-- && j)
    {
        string s1 = q.front();
        q.pop();

        p=1;x=0;

        if(s1.length()== l && s1[s1.length()-1]=='1')
        {
        	RFOR(i,s1.length(),0)
	        {
	        	x+=(s1[i]=='1')?p:0;
	        	p*=10;
	        }

	        f=test(x);

	        if(f==1)
	        {
	        	cout<<x<<x<<" ";
	        	j--;
	        	FOR(i,0,a.size())cout<<a[i]<<" ";
	        	cout<<endl;
	        }

	        a.clear();
        }
        
        string s2 = s1; 
  
        q.push(s1.append("0"));
 
        q.push(s2.append("1"));
    }
}


void solve()
{
	ll t,ans;char prev;string s,x;llu n,j;

	cin>>t;

	FOR(k,1,t+1)
	{	
		cin>>n>>j;
		cout<< "Case #" << k <<":\n";
		genbinary(n,j);
	}	
}

int main() 
{
	ios::sync_with_stdio(false);cin.tie(0);

	ld stime = gett();

	solve();

	cerr << "Time: "<< gett() - stime << endl;

	return 0;
}   
