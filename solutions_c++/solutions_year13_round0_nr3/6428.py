#include <cstdio>
#include <cstring>
#include <iostream>
#include <fstream>
int main()
{
	int test,i,j;
	scanf ( "%d", &test );
	int u = 1;
	while ( u<= test ) {
		char a[7][7];
		for ( i = 0; i < 4; i++) {
			scanf ( "%s", a[i] );
		}
		int y = 0,cx,cy,flag;
		for ( i = 0; i < 4; i++) {
			cx = 0,cy = 0,flag = 0;
			for ( j = 0; j < 4; j++) {
				if ( a[i][j] == 'X' ) {
					cx++;
				}else if ( a[i][j] == 'O' ) {
					cy++;
				}else if ( a[i][j] == 'T' ) {
					flag = 1;
				}
			}
			if ( cx == 3 && flag == 1  ) {
				printf ( "Case #%d: X won\n", u );
				y = 1;
				goto b;
			}else if ( cy == 3 && flag == 1 ) {
				printf ( "Case #%d: O won\n", u );
				y = 1;
				goto b;
			}else if ( cx == 4 || cy == 4 ) {
				if ( cx == 4 ) {
					printf ( "Case #%d: X won\n", u );
					y = 1;goto b;
				}else {
					printf ( "Case #%d: O won\n", u );
					y = 1;goto b;
				}
			}
			cx = cy = flag = 0;
		}
		for ( i = 0; i < 4; i++) {
			cx = cy = flag = 0;
			for ( j = 0; j < 4; j++) {
				if ( a[j][i] == 'X' ) {
					cx++;
				}else if ( a[j][i] == 'O' ) {
					cy++;
				}else if ( a[j][i] == 'T' ) {
					flag = 1;
				}
			}
			if ( (cx == 3 && flag == 1 ) ) {
				printf ( "Case #%d: X won\n", u );
				y = 1;
				goto b;
			}else if ( cy == 3 && flag == 1 ) {
				printf ( "Case #%d: O won\n", u );
				y = 1;
				goto b;
			}else if ( cx == 4 || cy == 4 ) {
				if ( cx == 4 ) {
					printf ( "Case #%d: X won\n", u );
					y = 1;
					goto b;
				}else {
					printf ( "Case #%d: O won\n", u );
					y = 1;goto b;
				}
			}

			cx = cy = flag = 0;
		}
		cx = cy = flag = 0;
		for ( i = 0; i < 4; i++) {
			if ( a[i][i] == 'X' ) {
				cx++;
			}else if ( a[i][i] == 'O' ) {
				cy++;
			}else if ( a[i][i] == 'T' ) {
				flag = 1;
			}
		}

		if ( cx == 3 && flag == 1 ) {
			printf ( "Case #%d: X won\n");
			y = 1;
			goto b;
		}else if ( cy == 3 && flag == 1 ) {
			printf ( "Case #%d: O won\n");
			y = 1;
			goto b;
		}else if ( cx == 4 || cy == 4 ) {
			if ( cx == 4 ) {
				printf ( "Case #%d: X won\n", u );
				y = 1;goto b;
			}else {
				printf ( "Case #%d: O won\n", u );
				y = 1;goto b;
			}
		}

		cx = cy = flag = 0;
		for ( i = 3; i >= 0; i--) {
			if ( a[3-i][i] == 'X' ) {
				cx++;
			}else if ( a[3-i][i] == 'O' ) {
				cy++;
			}else if ( a[3-i][i] == 'T' ) {
				flag = 1;
			}
		}
		//		printf ( "dcx = %d\tcy = %d\tflag = %d\n", cx, cy, flag);

		if ( cx == 3 && flag == 1 ) {
			printf ( "Case #%d: X won\n",u);
			y = 1;
			goto b;
		}else if ( cy == 3 && flag == 1 ) {
			printf ( "Case #%d: O won\n",u);
			y = 1;
			goto b;
		}else if ( cx == 4 || cy == 4 ) {
			if ( cx == 4 ) {
				printf ( "Case #%d: X won\n", u );
				y = 1;goto b;
			}else {
				printf ( "Case #%d: O won\n", u );
				y = 1;goto b;
			}
		}
		cx = cy = flag = 0;
b:
		if ( y != 1 ) {
			int flag1 = 0;
			for ( i = 0; i <4; i++) {
				for ( j = 0; j < 4; j++) {
					if ( a[i][j] == '.' ) {
						printf ("Case #%d: Game has not completed\n",u);
						flag1 = 1;
						goto c;
					}
				}
			}
c:
			if ( flag1 == 0 ) {
				printf ( "Case #%d: Draw\n", u );
			}
		}
		u++;
	}
	return 0;
}









