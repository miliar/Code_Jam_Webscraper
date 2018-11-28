#include <cstdlib>
#include <cstring>
#include <cassert>
#include <climits>
#include <cstdio>
#include <cctype>
#include <cfloat>
#include <ctime>

#include <algorithm>
#include <iostream>
#include <utility>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <numeric>
#include <complex>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <map>


#define forab(i,a,b) for( __typeof (a) i = a ; i <= b ; i++ )
#define forba(i,a,b) for( __typeof (a) i = a ; i >= b ; i-- )
#define rep(i,n) forab(i,0,n-1)
#define repr(i,n) forba(i,n-1,0)
#define forstl(i, s) for ( __typeof ((s).end ()) i = (s).begin (); i != (s).end (); i++ )

#define memo(a,b)       memset (a,b,sizeof(a))
#define all(a)          a.begin () , a. end ()
#define clr(a)          a.clear ()
#define sz(a)           a.size()
#define sf              scanf
#define pf              printf
#define si(a)           scanf("%d",&a)
#define pb              push_back
#define mp              make_pair
#define nl              puts("")
#define ll              long long
#define vi              vector < int >
#define vii				vector < int , int >
#define vll             vector < ll >
#define pii             pair < int , int >
#define endl			'\n'
#define swap(a,b)		a=a^b,b=b^a,a=a^b

#define rd              freopen ( "input.txt" , "r" , stdin )
#define wr              freopen ( "output.txt" , "w" , stdout )

using namespace std ;

int main()
{
	rd;wr;
	int a,b,k,t;
	

	scanf("%d",&t);
	for(int q=0;q<t;q++)
	{
		cin>>a>>b>>k;
		int cnt=0;
		for(int i=0;i<a;i++)
		{
			for(int j=0;j<b;j++)
			{
				if((i&j)<k)
				cnt++;
			}
		}
		printf("Case #%d: %d\n",q+1,cnt);
		// cout<<"Case #"<<q+1<<": ";
		// cout<<cnt<<endl;
	}
	
	
return 0;
}
