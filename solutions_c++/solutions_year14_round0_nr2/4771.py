#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <iomanip>
using namespace std;

#define for2(i,a,b) for(int i=a;i<b; i++ )
#define sz(a) (int)a.size ( )
#define all(a) a.begin ( ), a.end ( ) 
#define pb push_back
#define f1 first
#define f2 second
#define float double
#define eps 1e-9

bool comp ( float a, float b ){
	return  a - eps <= b + eps;
}

main ( ){
	int L;
	cin >> L;
	for2 ( test, 1, L+1 ){
		cout << "Case #" << test << ": ";
		float c, f, x;
		cin >> c >> f >> x;
		float minAns = -1;
		float now = 0, time1 = 0, d = 2;
		while ( 1 ){
//			cout << time1 << " " << minAns << endl;
			if ( minAns >= 0 && comp ( minAns, time1 ) )
			   break;	
			float nw = x / d;
			if ( minAns < 0 || comp ( nw + time1, minAns ) )
				minAns = nw + time1;
			time1 += c / d;
			d += f;
		}
		cout << fixed << setprecision(8) << minAns << endl;
	}
	
}
