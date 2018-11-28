#include <iostream>
	#include <cstdio>
	#include <cstring>
	#include <cstdlib>
	#include <cctype>
	#include <algorithm>
	#include <map>
	#include <vector>
	#include <list>
	#include <set>
	#include <queue>
	#include <deque>
	#include <stack>
	#include <string>
	#include <cmath>
	using namespace std;

	#define FOR(i,a,b) for(int i=a;i<b;i++)
	#define FORD(i,a,b) for(int i=a;i>=b;i--)
	#define REP(i,n) FOR(i,0,n)
	#define PB push_back
	#define ITER(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
	#define mod 1000000007
	#define MAXN 1000010

	typedef pair<int,int>   ii;
	typedef vector<int> VI;
	typedef long long ll;
	typedef vector<ll> vll;
	typedef vector<int> vi;
	typedef vector<vi> vvi;
	typedef vector<bool> vb;
	typedef vector<vb> vvb;

	const int MAXH = 1010;
	const int MAXW = 1010;
int main()
{
   int t;
   cin>>t;
   vi v(1001);
   v[1]=1;v[4]=1;v[9]=1;v[121]=1;v[484]=1;
   vi vc;
   REP(i,t)
   {
       int a,b;

       cin>>a>>b;
       int c=0;
       for(int j=a;j<=b;j++)
       {
           if(v[j]==1)
                c++;
       }
       vc.push_back(c);
   }
   REP(i,t)
        cout<<"Case #"<<i+1<<": "<< vc[i]<<endl;
    return 0;
}
