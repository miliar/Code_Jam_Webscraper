#include <bits/stdc++.h>

using namespace std;
const int N = 4;

char A[N], B[N];
int l,lim,pw[4]={1,10,100,1000};

bool okA(int a){
	for(int i = 0; i < l; i++){
		if(A[i] != '?' and (a % pw[l-i])/pw[l-i-1] != A[i] - '0') return 0;
	}
	return 1;
}

bool okB(int a){
	for(int i = 0; i < l; i++){
		if(B[i] != '?' and (a % pw[l-i])/pw[l-i-1] != B[i] - '0') return 0;
	}
	return 1;
}

int p,q,v;

void init(){
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++){
		scanf("%s",A);
		scanf("%s",B);
		l = strlen(A);
		lim = pw[l];
		p = q = v = 10000;
		for(int a = 0; a < lim; a++){
			if(!okA(a)) continue;
			for(int b = 0; b < lim; b++){
				if(!okB(b)) continue;
				int val = abs(a - b);
				if(val > v) continue;
				if(val == v){
					if(p < a) continue;
					if(p == a){
						if(q > b) q = b;
					}
					else p = a, q = b;
				}
				else v = val, p = a, q = b;
			}
		}
		if(l == 1) printf("Case #%d: %d %d\n",t,p,q);
		else if(l == 2) printf("Case #%d: %d%d %d%d\n",t,p/10,p%10,q/10,q%10);
		else if(l == 3) printf("Case #%d: %d%d%d %d%d%d\n",t,p/100,(p % 100)/10, p % 10,q/100,(q % 100)/10, q%10);
	}
}

void fread(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
}

int main(){
	fread();
	init();
	return 0;
}