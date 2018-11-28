#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
    int t;
    scanf ("%d", &t);

    int a[4][4], c_x, c_y, c_t,i,j, flag, not_completed,k;
    for (k=0;k<t;k++) {
	getchar();
        not_completed = 0;
        for (i=0; i<4; i++) {
            for (j=0; j<4; j++) {
                a[i][j]=0;
            }
        }
        for (i=0; i<4; i++) {
            for (j=0; j<4; j++) {
                scanf ("%c",&a[i][j]);
            }
	    getchar();
        }
	//for (i=0;i<4;i++){
	//	for (j=0;j<4;j++) 
	//		printf ("%c",a[i][j]);
	//	printf ("\n");
	//}
        // check diagonal
//        printf ("checking first diagonal\n");
        c_x = 0;
        c_y = 0;
        c_t = 0;
        for (i=0,j=0; i<4,j<4; i++,j++) {
            if (a[i][j] == 'X') {
                c_x ++;
            } else if (a[i][j]=='O') {
                c_y ++;
            } else if (a[i][j] =='T' ) {
                c_t++;
            }
        }
        if (c_x == 4 || (c_x == 3 && c_t == 1)) {
            printf ("Case #%d: X won\n",k+1);
            continue;
        } else if (c_y == 4 || (c_y == 3 && c_t == 1)) {
            printf ("Case #%d: O won\n", k+1);
            continue;
        }
        // check another diagonal
//        printf ("checking second diagonal\n");
        c_x = 0;
        c_y = 0;
        c_t = 0;
        for (i=3,j=0; i>=0,j<4; i--,j++) {
            if (a[i][j] == 'X') {
                c_x ++;
            } else if (a[i][j]=='O') {
                c_y ++;
            } else if (a[i][j] =='T' ) {
                c_t++;
            }
        }
        if (c_x == 4 || (c_x == 3 && c_t == 1)) {
            printf ("Case #%d: X won\n",k+1);
            continue;
        } else if (c_y == 4 || (c_y == 3 && c_t == 1)) {
            printf ("Case #%d: O won\n",k+1);
            continue;
        }
        // checking 4 rows
//        printf ("checking 4 rows\n");
        flag = 0;
        for (i=0; i<4; i++) {
            c_x = 0;
            c_y = 0;
            c_t = 0;
            for (j= 0; j < 4; j++) {
                if (a[i][j] == 'X') {
                    c_x ++;
                } else if (a[i][j]=='O') {
                    c_y ++;
                } else if (a[i][j] =='T' ) {
                    c_t++;
                } else if (a[i][j] == '.') {
		    not_completed = 1;
                }
            }
            if (c_x == 4 || (c_x == 3 && c_t == 1)) {
                printf ("Case #%d: X won\n",k+1);
                flag = 1;
                break;
            } else if (c_y == 4 || (c_y == 3 && c_t == 1)) {
                printf ("Case #%d: O won\n", k+1);
                flag = 1;
                break;
            }
        }
        if (flag == 1) {
            continue;
        }
        // checking 4 columns
//        printf ("checking 4 columns\n");
        for (j=0; j<4; j++) {
            c_x = 0;
            c_y = 0;
            c_t = 0;
            for (i=0; i<4; i++) {
                if (a[i][j] == 'X') {
                    c_x ++;
                } else if (a[i][j]=='O') {
                    c_y ++;
                } else if (a[i][j] =='T' ) {
                    c_t++;
                }
            }
            if (c_x == 4 || (c_x == 3 && c_t == 1)) {
                printf ("Case #%d: X won\n",k+1);
                flag = 1;
                break;
            } else if (c_y == 4 || (c_y == 3 && c_t == 1)) {
                printf ("Case #%d: O won\n",k+1);
                flag = 1;
                break;
            }
        }
        if (flag == 1) {
            continue;
        }
        if (not_completed == 1) {
            printf ("Case #%d: Game has not completed\n",k+1);
        } else {
            printf ("Case #%d: Draw\n",k+1);
        }
//	getchar();
    }
    return 0;
}
