#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

bool ok;
int N, M;
int myLawn[110][110];

bool check( int pattern, int x, int y ){
        int checkCol = 0;
		int checkRow = 0;
        for( int col=0; col<M; col++ ){
                if( myLawn[x][col] <= pattern ){
					checkCol++;
				} else {
					break;
				}
        }
 
        for( int row=0; row<N; row++ ){
			if( myLawn[row][y] <= pattern ){
				checkRow++;
			} else {
				break;
			}
        }
 
        if( checkCol == M || checkRow == N ){
			return true;
		} else {
			return false;
		}
}
 
int main(){
        int lawnmower;
		int count = 1;

        scanf_s( "%d", &lawnmower );
        while( lawnmower-- ){
			scanf_s( "%d%d", &N, &M );
			
			for( int i=0; i<N; i++ ){
				for( int j=0; j<M; j++ ){
					scanf_s( "%d", &myLawn[i][j] );
				}
			}
			
			ok = true;
			
			for( int i=0; i<N; i++ ){
				for( int j=0; j<M ; j++ ){
					int pattern = myLawn[i][j];
                    ok = check(pattern, i, j);
					if( !ok ) break;
				}

				if( !ok ) break;
			}
			
			printf("Case #%d: ", count++);

            if( ok ){
				puts("YES");
			} else {
				puts("NO");
			}
        }

        return 0;
}