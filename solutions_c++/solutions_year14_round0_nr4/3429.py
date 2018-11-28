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
#define MP              make_pair
#define nl              puts("")
#define ll             long long
#define vi              vector < int >
#define vii		vector < int , int >
#define vll             vector < ll >
#define pii             pair < int , int >

#define rd              freopen ( "input.txt" , "r" , stdin )
#define wr              freopen ( "output.txt" , "w" , stdout )

using namespace std ;

int main()
{
	rd;wr;
	int i,t,n;
	float a[1005],b[1005];
	cin>>t;
	for(int q=1;q<=t;q++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
		cin>>a[i];
		for(int i=0;i<n;i++)
		cin>>b[i];
		sort(a,a+n);sort(b,b+n);
		int ans1=0,cnt=n,i=n-1,j=n-1;
		while(cnt--)
		{
			if(a[i]>b[j])
			{j--;i--;ans1++;}
			else
			j--;
		}
		int ans2=0;
		cnt=n;i=n-1;j=n-1;
		while(cnt--)
		{
			if(a[i]>b[j])
			{i--;ans2++;}
			else
			{i--;j--;}
		}
		cout<<"Case #"<<q<<": "<<ans1<<" "<<ans2<<endl;
	}
return 0;	
}
