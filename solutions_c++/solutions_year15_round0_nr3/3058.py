#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <ctime>

using namespace std;
FILE *fin  = fopen("c.in",  "r");
FILE *fout = fopen("gcj-c.out", "w");

//  1 =>  1
//  2 =>  i
//  3 =>  j
//  4 =>  k
// -1 => -1
// -2 => -i
// -3 => -j
// -4 => -k
int qmat[4][4] = {{1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};
int qp(int a, int b) {
    if(a ==  1) return  b;
    if(a == -1) return -b;
    if(a ==  2) return ((b>0)?  qmat[1][b-1]: -qmat[1][-b-1]);
    if(a == -2) return ((b>0)? -qmat[1][b-1]:  qmat[1][-b-1]);
    if(a ==  3) return ((b>0)?  qmat[2][b-1]: -qmat[2][-b-1]);
    if(a == -3) return ((b>0)? -qmat[2][b-1]:  qmat[2][-b-1]);
    if(a ==  4) return ((b>0)?  qmat[3][b-1]: -qmat[3][-b-1]);
    if(a == -4) return ((b>0)? -qmat[3][b-1]:  qmat[3][-b-1]);
}

int a[10000];
int prod(int i1, int i2) {
    int cur = 1;
    for(int i = i1; i < i2; i++) {
        //cout << "\t" << cur << " * " << a[i] << " = ";
        cur = qp(cur, a[i]);
        //cout << cur << endl;
    }
    return cur;
}

int main () {
    int T, L, X; char c;
	fscanf(fin, "%d", &T);
	for(int t = 1; t <= T; t++) {
		fscanf(fin, "%d %d\n", &L, &X);
		cout << L << " " << X << endl;
		for(int i = 0; i < L; i++) {
            fscanf(fin, "%c", &c);
            //cout << c;
            if(c == 'i') a[i] = 2;
            if(c == 'j') a[i] = 3;
            if(c == 'k') a[i] = 4;
		}
		for(int i = 1; i < X; i++) {
            for(int j = 0; j < L; j++) {
                a[L * i + j] = a[j];
            }
		}
		//cout << prod(0, L*X) << endl;
		if(prod(0, L*X) != -1) {
            fprintf(fout, "Case #%d: NO\n", t);
            printf("Case #%d: NO\n", t);
            continue;
		}
		bool works = false;
		int curi = 1;
		for(int i = 1; i < X * L; i++) {
            curi = qp(curi, a[i-1]);
            int curj = 1;
            for(int j = i+1; j < X * L; j++) {
                curj = qp(curj, a[j-1]);
                if(curi == 2 && curj == 3) works = true;
            }
		}
		fprintf(fout, "Case #%d: %s\n", t, (works)? "YES":"NO");
		printf("Case #%d: %s\n", t, (works)? "YES":"NO");
	}
	return 0;
}
