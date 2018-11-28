#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;
int TT;
int x, r, c;
int rr;
void g(){
	printf("Case #%d: GABRIEL\n", rr);
}
void ri(){
	printf("Case #%d: RICHARD\n", rr);
}
int main() {
	scanf("%d", &TT);
	for(rr=1; rr<=TT; ++rr){
		scanf("%d%d%d", &x, &r, &c);
		if(x == 1){
			g();
		}else if(x==2){
			if(r * c % 2 == 0){
				g();
			}else ri();
		}else if(x==3){
			if((r * c % 3 == 0) && r!=1 && c!=1){
				g();
			}else ri();
		}else if(x==4){
			if(r>c) swap(r, c);
			if(c==4 && (r>=3)) g();
			else ri();
		}
	}
	return 0;
}

