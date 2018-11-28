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
	freopen("B-small-attempt0.in","r",stdin);
	int c = 1 , r  , t  ,a ,b , k  , f  ; 
	cin >> t ; 
	vector<int > v;
	while (t--)
	{
		f=0;
		v.clear();
		cin >> a >> b >> k ; 

		rep ( i , a ) 
			rep ( j , b ) {
				r = i & j ;
					v.push_back(r);
				//cout << r <<endl;
		}
		sort(v.begin() , v.end() ) ;
		rep( i , sz(v) )
		{
			if ( v[i] < k ) 
				f ++;
		}
		cout << "Case #"<<c++<<": "<<f<<endl;
	
	}




	return 0 ;
}

