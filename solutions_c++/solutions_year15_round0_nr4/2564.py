#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;
typedef long long ll;
#define DEBUG
#define mod 1000000007

int main(){
	//ios::sync_with_stdio(false);
	#ifdef DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif // DEBUG
	
	int T,R,C,X;
	scanf("%d", &T);
	for(int t=1;t<=T;t++){
		scanf("%d%d%d", &X, &R, &C);
		if(X==1){
			printf("Case #%d: %s\n", t, "GABRIEL");
		}
		else if(X==2){
			if((R*C)%2!=0)
				printf("Case #%d: %s\n", t, "RICHARD");
			else
				printf("Case #%d: %s\n", t, "GABRIEL");
		}
		else if(X==3){
			int ans=0;
			if((R==2 && C==3) || (R==3 && C==2))
				ans=1;
			if((R==4 && C==3) || (R==3 && C==4))
				ans=1;
			if((R==3 && C==3) || (R==3 && C==3))
				ans=1;
			if(ans==1)
				printf("Case #%d: %s\n", t, "GABRIEL");
			else
				printf("Case #%d: %s\n", t, "RICHARD");
		}
		else if(X==4){
			int ans=0;
			if((R==4 && C==3) || (R==3 && C==4))
				ans=1;
			if(R==4 && C==4)
				ans=1;
			if(ans==1)
				printf("Case #%d: %s\n", t, "GABRIEL");
			else
				printf("Case #%d: %s\n", t, "RICHARD");
		}
	}

	return 0;
}
