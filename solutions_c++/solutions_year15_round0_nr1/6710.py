using namespace std;
#include <bits/stdc++.h>
#define fr(i,a,b) for(int i = a; i < b; i++)
#define _ printf("\n");

int s;
int f;
char S[1010];


int dp(int i, int up, int inv){
//	printf("s:%d i:%d up:%d inv:%d\n",s,i,up,inv);
	if (i == s+1) return inv;
	
	int q = S[i] - '0';
	
	if (q > 0 && i > up){ 
		inv += i-up;
		up += i-up;
	}
	
	up += q;
//	printf("i:%d up:%d inv:%d q:%d\n",i,up,inv,q);
	
	return dp(i+1,up,inv);
	
}

int main(){	
	int T; scanf("%d",&T);
	fr(t,0,T){
		scanf("%d",&s);
		scanf("%s",S);
		f = dp(0,0,0);
		
		printf("Case #%d: %d\n",t+1,f);
		
	}

	return 0;
}

