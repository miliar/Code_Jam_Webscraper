#include<cstdio>
using namespace std;

int main(){
    int T, X, R, C;
    scanf(" %d ", &T);

    for(int t=1; t<=T; ++t){
	scanf(" %d %d %d ", &X, &R, &C);
	if(R*C < X){
	    printf("Case #%d: RICHARD\n", t);
	    continue;
	}
	if(R*C % X != 0){
	    printf("Case #%d: RICHARD\n", t);
	    continue;
	}
	if(X >= 3 && R*C == X){
	    printf("Case #%d: RICHARD\n", t);
	    continue;
	}
	if((R < C ? R : C) == 2 && (R > C ? R : C) == 4 && X == 4){
	    printf("Case #%d: RICHARD\n", t);
	    continue;
	}
	printf("Case #%d: GABRIEL\n", t);
    }

    return 0;
}
