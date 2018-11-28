#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;
#define for2(i,a,b) for(int i=a;i<b; i++ )
#define sz(a) (int)a.size ( )
#define all(a) a.begin ( ), a.end ( ) 
#define pb push_back
#define f1 first
#define f2 second

int a[4][4], b[4][4];

main ( ){
	int T;
	cin >> T;
	for2 ( TTT, 0, T ){
		int a1, b1;
		cin >> a1;
		cout << "Case #" << TTT+1 << ": ";
		for2 ( i, 0, 4 )
			for2 ( j, 0, 4 ) 
				cin >> a[i][j];
		cin >> b1;
		for2 ( i, 0, 4 )
			for2 ( j, 0, 4 )
				cin >> b[i][j];
		int num = 0, ind;
		for2 ( i, 0, 4 ){
			for2 ( j, 0, 4 ){
				if ( a[a1-1][i] == b[b1-1][j] )
						num++, ind = a[a1-1][i];
			}
		}
		if ( num == 1 )
			cout << ind << endl;
		else if ( num > 1 )
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl;
	}
}
