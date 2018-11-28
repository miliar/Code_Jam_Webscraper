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
	cin>>t;
	for(int q=1;q<=t;q++)
	{
		int a[5][5],b[5],r1,r2;
		cin>>r1;
		r1--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>a[i][j];
		}
		for(int i=0;i<4;i++)
		b[i]=(a[r1][i]);
		cin>>r2;
		r2--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>a[i][j];
		}
		int cnt=0,ans=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
				if(b[i]==a[r2][j])
				{ans=b[i];cnt++;}
		}
		
		if(cnt==0)
		cout<<"Case #"<<q<<": Volunteer cheated!\n";
		else if(cnt==1)
		cout<<"Case #"<<q<<": "<<ans<<endl;
		else
		cout<<"Case #"<<q<<": Bad magician!\n";
		
	}
return 0;	
}
