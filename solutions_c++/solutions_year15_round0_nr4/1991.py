#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
 
inline void fastRead_int(int &x) {
	register int c = getchar_unlocked();
	x = 0;
	for(; (c<48 || c>57); c = getchar_unlocked());
	for(; c>47 && c<58 ; c = getchar_unlocked()) {
	    x = (x<<1) + (x<<3) + c - 48;}};

int answer[4][4][4]= {  {{1,1,1,1},{1,1,1,1},{1,1,1,1},{1,1,1,1}},{{0,1,0,1},{1,1,1,1},{0,1,0,1},{1,1,1,1}},{ {0,0,0,0},{0,0,1,0},{0,1,1,1},{0,0,1,0}},{ {0,0,0,0},{0,0,0,0},{0,0,0,1},{0,0,1,1}} };

int main() {
	int tcases,rows,columns,omino;
    fastRead_int(tcases);
    for(int i =1; i<= tcases;i++){
        fastRead_int(omino);
        fastRead_int(rows);
        fastRead_int(columns);
        int ans = answer[omino-1][rows-1][columns-1];
        if(ans == 0){ printf("Case #%d: %s\n",i,"RICHARD");}
        else{  printf("Case #%d: %s\n",i,"GABRIEL"); }
    }
    return 0;
}
	