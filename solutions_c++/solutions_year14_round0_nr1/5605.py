#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<iostream>
#include<set>
#include<utility>
#include<algorithm>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for( int C = 1; C <= T; C ++ ){
		int R1, R2;
		vector<int> r1(16), r2(16);
		cin >> R1;
		for( int i = 0; i < 16; i ++ ){
			int j;
			cin >> j;
			r1[j-1] = i / 4 + 1;
		}
		cin >> R2;
		for( int i = 0; i < 16; i ++ ){
			int j;
			cin >> j;
			r2[j-1] = i / 4 + 1;
		}
		int c = 0;
		int ans = -1;
		for( int j = 0; j < 16; j ++ ){
			if( r1[j] == R1 && r2[j] == R2 ){
				c ++;
				ans = j;
			}
		}
		printf( "Case #%d: ", C );
		if( c == 1 )
			printf( "%d\n", ans + 1 );
		else if( c == 0 )
			printf( "Volunteer cheated!\n" );
		else
			printf( "Bad magician!\n" );
	}
}
