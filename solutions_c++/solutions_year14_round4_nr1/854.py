#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

#define fr(a,b,c) for(int a = b; a < c; a++)
#define rep(a,b) fr(a,0,b)
#define pb push_back
#define db if(1)
#define ln puts("")

int n;

int r[777];
int cap;

bool read(){
	scanf("%d%d", &n, &cap);
	
	memset(r, 0, sizeof r);
	
	rep(i,n){
		int a;
		scanf("%d", &a);
		r[a]++;
	}
	
	return true;
}

int cn = 1;

void process(){
	printf("Case #%d: ", cn++);

	int res = 0;
	
	for(int i = cap; i >= 1; i--){
		//printf("%d\n", i); fflush(stdout);
		for(int j = cap-i; j >= 1; j--){			
			while(r[i] && r[j]){
				//printf("%d %d %d %d\n", i, j, r[i], r[j]);
				if(i == j && r[i] < 2) break;
				r[i]--;
				r[j]--;
				//printf("used %d %d\n", i, j);
				res++;
			}
		}
	}
	
	rep(i,cap+1) res += r[i];
	
	printf("%d\n", res);
}

int main(){
	int t;
	scanf("%d", &t);
	
	while(t-- && read()) process();
	
	return 0;
}


