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

float a[2000], b[2000];
bool visited[2000], visited2[2000];

main ( ){
	int L;
	cin >> L;
	for2 ( test, 1, L+1 ){
		cout << "Case #" << test << ": ";
		memset ( visited, 0, sizeof(visited) );		
		memset ( visited2, 0, sizeof(visited2) );
		int n;
		cin >> n;
		for2 ( i, 0, n )
		 	cin >> a[i];
		for2 ( i, 0, n )
			cin >> b[i];
		sort ( a, a +n );
		sort ( b, b +n );
		int max1 = 0, max2 = 0, num = 0;
		for ( int i = n-1; i>=0; i-- ){
			for ( int j=n-1; j>=0; j-- ){
				if ( a[i] > b[j] && !visited2[j] ){
					visited2[j] = 1;
					max1++;
					break;
				}
			}	
		}
		cout << max1 << " ";
		for2 ( i, 0, n ){
			bool f = 0;
			for2 ( j, 0, n ){
				if ( b[j] > a[i] && !visited[j] ){
					visited[j] = 1;
					f = 1;
					break;
				}
			}
			if ( f )
				continue;
			for2 ( j, 0, n ){
				if ( !visited[j] ){
					visited[j] = 1;
					break;
				}
			}
			max2++;
		}
		cout << max2 << endl;
	}
}
