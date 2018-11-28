#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <utility> 
#include <stack>
#include <cstring> 
#include <cmath>
#include <stdio.h>
#include <string.h>
#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define oo ((int) 1e9)
#define mp make_pair

using namespace std;
int  main()
{
	//freopen("test.in" , "rt" , stdin);
	freopen("out.in","w",stdout);
	freopen("A-small-attempt3.in","r",stdin);
	int  t   , n  , c = 1 , r  , r2 , r1 ; 
	cin >> t  ;
	vector<string > s ; 
	string a , b , a1 , b1 ;
	bool f ;
	while ( t-- ) 
	{
		r=0;
		f=false;
		cin >> n ; 
		cin >> a >> b ; 
		a1 = "" ; b1 = "";
		int i = 0 ; 

		if ( sz(a) != 1 ) 
		{
		for (  i = 1 ; i < sz(a) ; i++) 
			if(a[i-1] != a[i] ) 
				a1+=a[i-1];

		if ( a1.empty() )
			a1+= a[0];
		else if ( a1[sz(a1) -1 ] != a[i-1]  )
			a1+=a[i-1];
		}
		else 
			a1 = a ; 

		if ( sz(b) != 1 ) 
		{
		for (  i = 1 ; i < sz(b) ; i++) 
			if(b[i-1] != b[i] ) 
				b1+=b[i-1];

		if ( b1.empty() ) 
			b1+=b[0] ;
		else if(b1[sz(b1) -1 ] != b[i-1] ) 
			b1+=b[i-1];

		}
		else 
			b1 = b ;

		if ( a1 != b1 ) 
			f= true;
		else 
		{
			r1= 0 ;
			r2 = 0 ;
			int j = 0 , k = 0  ; 
			for ( int i  = 0 ; i < sz(a1) ; i++) 
			{
				for ( r1 = 0; j < sz(a) ; j++) 
				{
					if ( a[j] == a1[i] )
						r1++ ;
					else 
					   break;
				}

				for ( r2 = 0 ; k < sz(b) ; k++) 
					if ( b[k] == a1[i] )
						r2++;
					else 
						break;
				//cout << r2 << " " << r1 << endl;
				r = r + (max (r1 , r2 ) ) - min ( r1 , r2 ) ;
			}
		}

		if ( f )
		   cout << "Case #"<<c++<<": Fegla Won"<<endl;
		else 
		   cout << "Case #"<<c++<<": "<<r<<endl;


	}
	return 0 ;
}

