#include <iostream>
#include <algorithm>
#include <cstdio>
#define FOR(i,l,r) for(int i = l; i <= r; i++)
#define ROF(i,r,l) for(int i = r; i >= l; i--)
#define INF 100000000
#define N 1010
using namespace std;

int num[N];

void deal(int T){
	int n,ans,s,x,x_max = 0;
	cin >> n;
	FOR(i,1,n){
		scanf("%d",&x);
		num[x] ++;
		if(x > x_max) x_max = x;
	}

	ans = INF;

	FOR(i,1,x_max) {
		s = 0;
		FOR(j,i + 1,x_max) if(num[j]>0){
			int k = j/i + (j%i > 0) - 1;
			s += k * num[j];
		}
		if(s + i < ans)ans = s + i;
	}
	
	printf("Case #%d: %d\n",T,ans);
	FOR(i,0,x_max) num[i] = 0;
}

int main(){
	freopen("data.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	int T;
	cin >> T;
	FOR(i,1,T) deal(i);
	return 0;
}
