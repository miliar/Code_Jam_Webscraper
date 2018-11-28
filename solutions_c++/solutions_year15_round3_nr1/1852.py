#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cmath>

using namespace std;

const int MAXN = 25;
int R,C,W;

int main(){
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		scanf("%d%d%d",&R,&C,&W);
		printf("Case #%d: %d\n",i,R*(C/W + W - (C%W == 0 ? 1 : 0)));
	}
}
