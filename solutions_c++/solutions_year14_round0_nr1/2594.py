#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <string>
using namespace std;
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define PRINTCASE printf("Case #%d: ",case_n++)
#define PRINTCASE_ printf("Case #%d:\n",case_n++)
#define RD(a) scanf("%d", &a)
#define RDD(a, b) scanf("%d%d", &a, &b)

int go(int row1, int mtx1[4][4], int row2, int mtx2[4][4], int *o){
	bool found = false;
	for(int i = 0; i < 4; ++i){
		int t = mtx1[row1 - 1][i];
		for(int j = 0; j < 4; ++j){
			if(mtx2[row2 - 1][j] == t){
				*o = t;
				if(found){
					return 1;
				}
				found = true;
			}
		}
	}
	return found ? 0 : 2;
}

int main(){
	int mtx1[4][4], mtx2[4][4];
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	CASET{
		int row1, row2;
		RD(row1);
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				scanf("%d", &mtx1[i][j]);
			}
		}
		RD(row2);
		for(int i = 0; i < 4; ++i){
			for(int j = 0; j < 4; ++j){
				scanf("%d", &mtx2[i][j]);
			}
		}
		PRINTCASE;
		int o;
		int type = go(row1, mtx1, row2, mtx2, &o);
		if(type == 0){
			cout << o << endl;
		}else if(type == 1){
			cout << "Bad magician!" << endl;
		}else{
			cout << "Volunteer cheated!" << endl;
		}
	}
	return 0;
}