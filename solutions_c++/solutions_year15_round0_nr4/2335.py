#include <iostream>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <math.h>
#include <limits.h>
#include <cstdlib>
#include <string.h>
#include <vector>
#include <map>
using namespace std;
//mehulagarwal
#define ll         long long
#define S(x)       scanf("%d", &x)
#define Sl(x)      scanf("%lld", &x)
#define Sd(x)      scanf("%lf", &x)
#define P(x)       printf("%d\n", x)
#define Pl(x)      printf("%lld\n", x)
#define Pd(x)      printf("%lf\n", x)
#define Pblank()   printf(" ")
#define mem(x,y)   memset(x,y,sizeof(x))
#define F(x,y,z,i) for (x = y; x < z; x = x + i)
#define mod 1000000007

int main()
{
    FILE *fi,*fo;
    int cid,t,n,i,j,x,r,c;
    fi = fopen("inp_d.txt","r");
    fo = fopen("out_d.txt","w+");
	int a[5][5][5];
	memset(a,0,sizeof(a));


	for (i = 1; i < 5; i++) {
        for (j = 1; j < 5; j++) {
            a[1][i][j] = 2;
        }
	}
	//a[1][1][1] = 1;

	for (i = 1; i < 5; i++) {
        for (j = 1; j < 5; j++) {
            a[2][i][j] = 2;
        }
	}
	a[2][1][1] = 1;
	a[2][1][3] = a[2][3][1] = a[2][3][3] = 1;

	for (i = 1; i < 5; i++) {
        for (j = 1; j < 5; j++) {
            a[3][i][j] = 1;
        }
	}
	a[3][3][2] = a[3][3][3] = a[3][3][4] = a[3][2][3] = a[3][4][3] = 2;
	//a[3][2][3] = a[3][3][2] = 2;

	for (i = 1; i < 5; i++) {
        for (j = 1; j < 5; j++) {
            a[4][i][j] = 1;
        }
	}
	a[4][3][4] = a[4][4][3] = a[4][4][4] = 2;
/*
	for (int k = 1; k < 5; k++) {
        for (i = 1; i < 5; i++) {
            for (j = 1; j < 5; j++) {
                cout << a[k][i][j] << " ";
            } cout << endl;
        } cout << endl << endl;
	}
*/

	fscanf(fi,"%d",&t);
	//cin >> t;
	for (cid = 1; cid <= t; cid++) {
        //cin >> x >> r >> c;
        fscanf(fi,"%d %d %d",&x,&r,&c);
        if (a[x][r][c] == 1) {
            //cout << "Case #" << cid << ": " << "RICHARD\n";
            fprintf(fo,"Case #%d: RICHARD\n",cid);
        } else if (a[x][r][c] == 2) {
            //cout << "Case #" << cid << ": " << "GABRIEL\n";
            fprintf(fo,"Case #%d: GABRIEL\n",cid);
        }
	}

	return 0;
}
