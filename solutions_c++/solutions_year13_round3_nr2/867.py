#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <string.h>
#include <queue>
#include <utility>
#include <time.h>
#include <string.h>
using namespace std;
int dx[] = {0,0,+1,-1};
int dy[] = {+1,-1,0,0};
char dd[] = "NSEW";

int main()
{
	int T;
	cin >> T;
	srand(time(NULL));
	for( int C = 1; C <= T; C ++ ){
		int X, Y;
		cin >> X >> Y;
		again:;
		int x = 0, y = 0;

		string ans = "";
		x = y = 0;
		ans = "";
		int t;
		for( t = 1; t < 501 && (x != X || y != Y); t ++ ){
			int d;
			do{
				d = rand() % 4;
			} while(0 && !(abs(x+dx[d]*t) < 200 && abs(y+dy[d]*t) < 200) );
			x += dx[d]*t;
			y += dy[d]*t;
			ans += dd[d];
		}
		if( t > 500 ) { goto again; }
		cout << "Case #" << C << ": " << ans << endl;
	}
	return 0;
}
