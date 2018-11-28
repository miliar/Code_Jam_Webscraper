#include <cstdio>
#include <algorithm>
#include <array>
#include <cstring>
using namespace std;

void solve(int X, int R, int C){
	int m=(X+1)/2;
	if(X>=7 || (R*C)%X!=0 || (R<X && C<X) || (R<m || C<m)){
		printf(" RICHARD\n");
		return;
	}
	if(X>3 && (R<=m || C<=m)){
		printf(" RICHARD\n");
		return;
	}
	printf(" GABRIEL\n");
}

void parse(void){
	int result;
	int X, R, C;
	result=scanf("%d%d%d", &X, &R, &C);
	solve(X, R, C);
	static_cast<void>(result);
}

int main(void){
	int test;
	int result=scanf("%d", &test);
	for(int i=1;i<=test;++i){
		printf("Case #%d:", i);
		parse();
	}
	static_cast<void>(result);
	return 0;
}
